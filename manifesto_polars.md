---
title: "The Query Plan"
tagline: "data moves through expressions, not into variables"
version: "1.0.0"
theme: "computational-model"
description: "Stop writing instructions. Describe results. Let the optimizer decide. The query plan is the program."
---

# THE QUERY PLAN
## The Manifesto of the Lazy Evaluation

*After Codd, Stonebraker, and the Polars optimizer*

---

## The Blindness

**You think in rows. You should think in plans.**

For thirty years, data scientists wrote imperative loops. Load the CSV. Filter the rows. Join the tables. Write the output. Each step materialized a DataFrame in RAM. Each variable held a snapshot of the world at one moment in the computation.

Polars does not work this way. Polars builds a directed acyclic graph of your intent, optimizes it, and executes the whole thing at once. The intermediate DataFrames never exist. The data never stops moving.

Yet programmers write `df = lf.collect()` on line 3, then spend forty lines manipulating `df` with eager operations. They have a lazy engine and use it as a warehouse.

We went to columnar vectorization before we stopped writing row loops.

This is **Imperative Blindness**. You see data as something you hold. Polars sees data as something that flows.

---

## The Enemy

Your enemy is **pandas thinking**.

It is the muscle memory of a decade. It is `.iterrows()` dressed in `.with_columns()`. It is the assumption that data must be materialized before it can be transformed.

The enemy speaks in familiar patterns:
- "Let me collect this so I can inspect it."
- "I'll chunk it in Python for memory safety."
- "Convert to numpy — Polars can't do this."

These are capitulations. Each one abandons the query optimizer. Each one forces the data to stop, sit in RAM, and wait for your Python loop to crawl through it.

---

## The Distinction: Imperative vs. Declarative

There are two computational models.

**The Imperative Model** issues commands. Load this. Filter that. Join these. Each command executes immediately. Each result occupies memory. The programmer sequences operations. The machine obeys.

**The Declarative Model** describes outcomes. "I want rows where price exceeds 100, joined with inventory, grouped by warehouse." The engine decides *how* — which predicates to push down, which columns to project, which joins to reorder, whether to stream or materialize.

| Imperative (pandas thinking) | Declarative (Polars thinking) |
|------------------------------|-------------------------------|
| Load all data, then filter | Scan with predicates pushed to source |
| Materialize, then transform | Transform within the query plan |
| Python loops for batching | Streaming engine handles memory |
| **Cost:** O(RAM) per step | **Cost:** O(plan) total |

**You write imperative code in a declarative engine.** Stop.

---

## The Axioms

### 1. The query plan is the program

You do not write instructions. You describe the result. Polars decides how to execute. Every `.collect()` is a decision to abandon this optimization.

```python
# This is not three operations. This is one query plan.
lf = (
    pl.scan_parquet("offers.parquet")
    .filter(pl.col("price") > 0)
    .join(categories, on="category_id")
    .group_by("department")
    .agg(pl.col("price").mean())
)
# Nothing has executed. No RAM consumed. No data read.
# Polars holds a plan, not a result.
```

Call `.explain()` before `.collect()`. Read the plan. Understand what the optimizer did. If you cannot read the plan, you do not understand your program.

### 2. Data never moves

The ideal pipeline: scan, transform, sink. Data flows from disk through expressions to disk. It never sits in RAM as a materialized DataFrame unless you force it.

```python
(
    pl.scan_csv("raw.csv", schema_overrides={"sku": pl.Utf8})
    .filter(pl.col("domain") != "internal")
    .with_columns(pair_id=canonical_id_expr)
    .sink_parquet("processed.parquet")
)
# Data streamed from CSV to Parquet. Peak RAM: one batch.
```

Every variable that holds a `DataFrame` is a dam in the river. Remove it.

### 3. Expressions are composable atoms

`pl.col("x").hash(seed=42).mod(100)` is not three operations. It is one expression that Polars fuses into a single vectorized pass. Build complex logic from expression composition, not Python control flow.

```python
# One expression. Polars fuses it. No intermediate allocations.
canonical_id = (
    pl.when(pl.col("domain_left") < pl.col("domain_right"))
    .then(pl.concat_str("domain_left", "sku_left", "domain_right", "sku_right",
                         separator="|"))
    .otherwise(pl.concat_str("domain_right", "sku_right", "domain_left", "sku_left",
                              separator="|"))
    .alias("pair_id")
)
```

If you extract a Polars column to a Python variable and manipulate it, you broke the expression graph. The optimizer cannot see through Python.

### 4. Types are contracts

`pl.Array(Float32, 1024)` is not decoration. It is a promise that enables SIMD vectorization, zero-copy reads, and columnar compression. Use `schema_overrides` at scan time. Post-hoc `.cast()` means you already loaded the wrong types into memory.

```python
# Types declared at the source. No cast needed downstream.
lf = pl.scan_csv(
    "offers.csv",
    schema_overrides={"sku": pl.Utf8, "price": pl.Float64},
)

# Schema validation without loading data.
schema = lf.collect_schema()
assert set(schema.names()) >= {"sku", "price", "domain"}
```

### 5. Every materialization has a budget

Before any operation that produces rows in RAM — `.collect()`, `.to_list()`, `concat`, `join(how="cross")`, `.to_numpy()` — compute the output size: `row_count × row_bytes × copies`. If the result exceeds `available_RAM / 4`, the operation is wrong. Chunk it, checkpoint it, or redesign it.

```python
# Budget: 8K clients × 10K competitors × 768 dims × 4 bytes × 2 sides = 470GB.
# This arithmetic takes 5 seconds. The OOM takes 5 hours to debug.
# Wrong: full cross-join
client_emb.lazy().join(competitor_emb.lazy(), how="cross")

# Right: chunk by client offer (~30MB per chunk)
for row in client_emb.iter_rows(named=True):
    single.lazy().join(competitor_emb.lazy(), how="cross")
    .sort("cosine_similarity", descending=True).head(k).collect()
```

A cross-join of N × M rows is not an N × M join. It is N × M × row_bytes bytes. Compute the number before writing the code. The streaming engine does not protect you — streaming batches have a size too (`POLARS_STREAMING_CHUNK_SIZE × row_bytes`).

---

## The Sins

### 1. Premature collection

`.collect()` then filter, transform, or join is the original sin. It materializes the entire dataset, destroying the query optimizer's ability to push predicates down, project columns away, or reorder joins.

**The test:** If code reads `.collect()` followed by `.filter()` or `.join()`, the author surrendered the query plan.

**The fix:** Keep the LazyFrame lazy. Chain operations. Collect once, at the boundary where Polars-land ends and Python-land begins.

### 2. Python-level batching

Writing `for batch in chunks:` around Polars operations admits defeat. The streaming engine exists. `sink_parquet()` streams results to disk without holding the full dataset in memory. If you chunk in Python, you replaced the query optimizer with a for-loop.

**The test:** If a Python loop wraps Polars operations, the author bypassed the streaming engine.

**The fix:** Use `engine="streaming"` in `.collect()`. Use `.sink_parquet()` for disk output. Let Polars manage batches.

### 3. The numpy escape hatch

Converting to numpy for computation that Polars can perform — distance, dot products, aggregations — wastes the query plan and forces materialization. `polars-distance` operates on Array columns natively. `Expr.dot()` exists. Leaving Polars-land has a cost: the data stops, copies, loses its columnar layout, and never returns to the plan.

**The test:** If `to_numpy()` precedes computation that Polars expressions can perform, the author paid an unnecessary toll.

**The fix:** Search the API first. Use `polars_search_api` to confirm whether an operation exists before escaping to numpy. Escape only at the final boundary — metrics computation, model training, visualization.

### 4. Dictionary lookups replacing joins

Building `dict[key, index]` for O(1) lookup is pandas thinking. Polars joins are the lookup. They are vectorized, parallelized, and streaming-compatible. A Python dictionary is single-threaded and forces materialization of both sides.

**The test:** If a `dict` is built from a DataFrame column for later lookup, the author reimplemented `join` in Python.

**The fix:** Use `.join()` with appropriate `how=` strategy. Anti-joins for exclusion. Left joins for enrichment. Inner joins for intersection.

### 5. Eager schema inference

`pl.read_csv()` instead of `pl.scan_csv()`. Loading data to discover its schema defeats lazy evaluation before the pipeline starts. The first line of the program already materialized the entire file.

**The test:** If `pl.read_` appears where `pl.scan_` could, the author loaded data to discover what it looked like.

**The fix:** `scan_csv`, `scan_parquet`, `scan_ndjson`. Always. Use `.collect_schema()` to inspect types without loading data. Use `schema_overrides` to enforce contracts at the source.

### 6. Unbudgeted materialization

Writing code that produces a DataFrame, numpy array, or Python collection without computing its size first. The streaming engine does not save you — streaming batches have a size too. If you cannot state the peak memory of your operation in bytes before running it, you do not understand your program.

**The test:** If the commit message or code comment does not contain a memory estimate for any operation that materializes data exceeding 1M rows, the author did not compute the budget.

**The fix:** Before every `.collect()`, `.sink_parquet()`, cross-join, or numpy conversion on large data, add a comment: `# Budget: N rows × M bytes/row = X GB`. If X > available_RAM / 4, restructure.

---

## The Patterns

### 1. scan, chain, sink — The canonical shape

Every pipeline has one shape. Scan from disk. Chain lazy transformations. Sink to disk. Everything between scan and sink is a query plan, not execution.

```python
(
    pl.scan_parquet("universe.parquet")
    .join(matches.lazy(), on=["domain", "sku"], how="left")
    .with_columns(label=pl.col("match_id").is_not_null().cast(pl.Int8))
    .filter(pl.col("domain_left") != pl.col("domain_right"))
    .sink_parquet("labeled_universe.parquet")
)
```

### 2. join_where for filtered cross-joins

Do not cross-join then filter. `join_where` pushes predicates into the join. The filtered rows never materialize.

```python
# Canonical deduplication: left < right prevents AB/BA duplicates.
pairs = offers.join_where(
    offers,
    pl.col("id") < pl.col("id_right"),
    suffix="_right",
)

# Multi-predicate blocking: all predicates AND-ed.
blocked = offers.join_where(
    offers,
    pl.col("id").str.contains(core_vendor),
    ~pl.col("id_right").str.contains(core_vendor),
    pl.col("cluster").list.contains(pl.col("cluster_right")),
    suffix="_right",
)
```

### 3. Array columns for embeddings

`pl.Array(Float32, D)` keeps embeddings in columnar storage. `polars-distance` operates on Array columns without conversion. Embeddings that leave Polars-land for numpy computation lose their columnar advantage.

### 4. Hash-based lazy partitioning

`pl.col("id").hash(seed) % N` produces deterministic, lazy, streaming-compatible partitions. No collection needed. No sklearn dependency for simple random splits.

```python
# Deterministic 80/20 split without leaving lazy mode.
train = universe.filter(pl.col("pair_id").hash(seed=42) % 100 < 80)
eval_ = universe.filter(pl.col("pair_id").hash(seed=42) % 100 >= 80)
```

Hash stability is guaranteed within a single Polars version. For cross-version reproducibility, sink the split to parquet and scan it back.

### 5. sink_parquet for checkpoints

Intermediate results go to parquet via `sink_parquet()`, read back with `scan_parquet()`. This is Polars' version of caching. The data touches disk, not RAM. The downstream scan gets full predicate and projection pushdown.

```python
def cached_transform(cache_path: Path, recompute: bool = False) -> pl.LazyFrame:
    if cache_path.exists() and not recompute:
        return pl.scan_parquet(cache_path)
    result = expensive_lazy_chain()
    result.sink_parquet(cache_path)
    return pl.scan_parquet(cache_path)
```

### 6. Anti-joins for exclusion

Do not filter by `~col.is_in(exclusion_list)`. Anti-joins are vectorized, parallelized, and lazy. They express intent directly: "rows from the left that have no match in the right."

```python
# Remove known positives from the negative candidate pool.
negatives = all_pairs.join(positive_pairs, on="pair_id", how="anti")
```

### 7. schema_overrides at scan time

Set types at the source. Not with `.cast()` after loading. Not with `infer_schema_length=10000`. With explicit contracts.

```python
lf = pl.scan_csv(
    "offers.csv",
    schema_overrides={"sku": pl.Utf8, "domain": pl.Utf8, "price": pl.Float64},
)
```

---

## The Composability Principle

Strategies — blocking, sampling, splitting, labeling — are `LazyFrame -> LazyFrame` transformations. They compose by function application. No strategy needs to know about the others.

```python
universe = build_pairs(offers)              # LazyFrame
blocked  = block_by_cluster(universe)       # LazyFrame -> LazyFrame
sampled  = hash_subsample(blocked, 0.1)     # LazyFrame -> LazyFrame
train, val, eval_ = split(sampled)          # LazyFrame -> 3 LazyFrames
train.sink_parquet("train.parquet")          # LazyFrame -> disk
```

Each function receives a LazyFrame and returns a LazyFrame. The query plan accumulates. Polars optimizes the entire chain when `sink_parquet` triggers execution. No function materializes data. No function knows whether it operates on ten rows or ten billion.

This is the architecture: a pipeline of composable, lazy, streaming-compatible transformations. The query plan grows until it hits a sink. Then the optimizer runs once, over the entire graph.

---

## The Choice

You stand at a divergence.

**Path 1: The Imperative.**
Collect early. Loop in Python. Escape to numpy. Build dictionaries. Chunk manually. Treat Polars as a faster pandas.
**Result:** You will fight memory, fight performance, and fight the engine that was built to help you.

**Path 2: The Declarative.**
Scan lazily. Compose expressions. Let the optimizer decide. Sink to disk. Touch RAM only at the boundary where Polars-land ends and the model begins.
**Result:** Your pipeline will stream through datasets it cannot fit in memory, optimize joins you did not think to reorder, and execute in parallel without a single thread annotation.

Stop writing instructions.
**Describe the result.**
