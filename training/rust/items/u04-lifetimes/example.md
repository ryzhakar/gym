# u04 worked example · lifetimes

Four subgoals. Every problem in this unit is solved by working through them in this order.

1. **Find where the returned reference comes from.** Trace each output reference to the input (or field) it borrows from; a reference to a local cannot leave.
2. **Name that link in the signature.** Elision covers one input reference and `&self` methods; otherwise declare a lifetime and tie the output only to the inputs it borrows from, never to an input it does not.
3. **Carry the lifetime through a struct.** A struct holding a reference declares `<'a>`; its impl declares it; a method returns `&'a T` when the result borrows the held data, `&T` when it borrows the struct.
4. **Make the borrow end before the conflict.** A borrow lives to its last use; reorder so it ends before a mutation or a move, or own the value where the data must outlive its source.

## The problem

Split a URL such as `"https://example.com/docs/intro"` into its parts without copying any text: scheme `"https"`, host `"example.com"`, path `"/docs/intro"`. Every part is a `&str` pointing into the caller's URL.

## Subgoal 1 · Find where the returned reference comes from

```rust
pub fn host(url: &str) -> &str {
    let rest = match url.split_once("://") {
        Some((_, rest)) => rest,
        None => url,
    };
    match rest.split_once('/') {
        Some((host, _)) => host,
        None => rest,
    }
}

pub fn with_scheme(url: &str) -> &str {
    let full = format!("https://{url}");
    &full
}
```

Trace each returned reference back:

| function | returns | which borrows from |
|---|---|---|
| `host` | `host` or `rest` | `rest`, which borrows from `url` |
| `with_scheme` | `&full` | `full`, a `String` built inside the function |

`host` hands back a piece of the caller's text, which outlives the call. `with_scheme` hands back a piece of `full`, which is dropped when the function returns:

```
error[E0515]: cannot return reference to local variable `full`
14 |     &full
   |     ^^^^^ returns a reference to data owned by the current function
```

No signature can fix this: the text `"https://example.com"` exists nowhere in the input. The function built new data, so it returns the owner:

```rust
pub fn with_scheme(url: &str) -> String {
    format!("https://{url}")
}
```

`host` needs no lifetime written: it has one input reference, and elision ties the output to it.

Predict: `host` returns a slice of `url`; `with_scheme` returns a slice of a `String` it built. Which of the two compiles as written, and why not the other?

## Subgoal 2 · Name that link in the signature

The path is whatever follows the host. The caller passes the host it already knows:

```rust
pub fn path_of(url: &str, host: &str) -> &str {
    match url.split_once(host) {
        Some((_, path)) => path,
        None => "",
    }
}
```

Two input references, so elision gives up:

```
error[E0106]: missing lifetime specifier
1 | pub fn path_of(url: &str, host: &str) -> &str {
  |                     ----        ----     ^ expected named lifetime parameter
  = help: this function's return type contains a borrowed value, but the signature does not say whether it is borrowed from `url` or `host`
help: consider introducing a named lifetime parameter
1 | pub fn path_of<'a>(url: &'a str, host: &'a str) -> &'a str {
```

The suggestion compiles, but it claims too much: it says the path may borrow from `host` as well. Subgoal 1 says otherwise: `path` is a piece of `url`, and `""` is a literal that lives forever. A caller whose `host` is gone before it reads the path is now refused:

```rust
let url = String::from("https://example.com/docs/intro");
let path;
{
    let host = String::from("example.com");
    path = path_of(&url, &host);
}
println!("{path}");
```

```
error[E0597]: `host` does not live long enough
13 |         path = path_of(&url, &host);
   |                              ^^^^^ borrowed value does not live long enough
14 |     }
   |     - `host` dropped here while still borrowed
15 |     println!("{path}");
   |                ---- borrow later used here
```

The error sits in the caller, but the fault is in the signature. Tie the output to `url` alone and leave `host` with its own, unnamed lifetime:

```rust
pub fn path_of<'a>(url: &'a str, host: &str) -> &'a str {
```

The caller compiles. When the result can come from either of two inputs, both get `'a`, and only those two:

```rust
pub fn path_or<'a>(url: &'a str, host: &str, fallback: &'a str) -> &'a str {
    let path = path_of(url, host);
    if path.is_empty() {
        fallback
    } else {
        path
    }
}
```

Predict: the compiler suggests one lifetime `'a` on `url`, `host` and the result. Does the caller that drops `host` before printing `path` compile under that signature?

## Subgoal 3 · Carry the lifetime through a struct

One struct holds all three parts. A field that is a reference needs a lifetime, just as a signature does:

```rust
pub struct Url {
    scheme: &str,
    host: &str,
    path: &str,
}
```

```
error[E0106]: missing lifetime specifier
2 |     scheme: &str,
  |             ^ expected named lifetime parameter
help: consider introducing a named lifetime parameter
1 ~ pub struct Url<'a> {
2 ~     scheme: &'a str,
```

(The same error follows for `host` and `path`.) With `pub struct Url<'a>` and every field `&'a str`, the impl must say which lifetime it is about:

```
error[E0726]: implicit elided lifetime not allowed here
7 | impl Url {
  |      ^^^ expected lifetime parameter
help: indicate the anonymous lifetime
7 | impl Url<'_> {
```

`Url<'_>` compiles, but leaves the lifetime nameless, and the methods below need to name it. Declare it instead: `impl<'a> Url<'a>`.

```rust
impl<'a> Url<'a> {
    pub fn parse(url: &'a str) -> Url<'a> {
        let (scheme, rest) = match url.split_once("://") {
            Some(parts) => parts,
            None => ("", url),
        };
        let (host, path) = match rest.find('/') {
            Some(i) => (&rest[..i], &rest[i..]),
            None => (rest, ""),
        };
        Url { scheme, host, path }
    }

    pub fn host(&self) -> &str {
        self.host
    }
}

pub fn host_of(url: &str) -> &str {
    let parts = Url::parse(url);
    parts.host()
}
```

`host(&self) -> &str` is elided to the lifetime of `&self`: it claims the host borrows from the `Url` value. So `host_of` may not return it, because `parts` is a local:

```
error[E0515]: cannot return value referencing local variable `parts`
35 |     parts.host()
   |     -----^^^^^^^
   |     |
   |     returns a value referencing data owned by the current function
   |     `parts` is borrowed here
```

Subgoal 1 again: the host is a piece of the caller's URL, held by the struct, not owned by it. Say so:

```rust
    pub fn host(&self) -> &'a str {
        self.host
    }
```

`host_of` compiles. The other direction holds too: a struct that owns data returns `&T` for it, tied to `&self`. Claiming `'a` for an owned field is refused:

```rust
pub struct Visit<'a> {
    url: &'a str,
    note: String,
}

impl<'a> Visit<'a> {
    pub fn note(&self) -> &'a str {
        &self.note
    }
}
```

```
error: lifetime may not live long enough
11 |     pub fn note(&self) -> &'a str {
   |                 - let's call the lifetime of this reference `'1`
12 |         &self.note
   |         ^^^^^^^^^^ method was supposed to return data with lifetime `'a` but it is returning data with lifetime `'1`
```

`note` dies with the `Visit`, so `pub fn note(&self) -> &str` is the honest signature.

Predict: with `host(&self) -> &str`, does `host_of`, which builds a `Url` inside itself and returns `parts.host()`, compile?

## Subgoal 4 · Make the borrow end before the conflict

The caller owns the URL and wants to change it:

```rust
let mut url = String::from("https://example.com/docs");
let parts = Url::parse(&url);
url.push_str("/intro");
println!("host {}", parts.host());
```

```
error[E0502]: cannot borrow `url` as mutable because it is also borrowed as immutable
36 |     let parts = Url::parse(&url);
   |                            ---- immutable borrow occurs here
37 |     url.push_str("/intro");
   |     ^^^^^^^^^^^^^^^^^^^^^^ mutable borrow occurs here
38 |     println!("host {}", parts.host());
   |                         ----- immutable borrow later used here
```

A borrow lasts until its last use, not to the end of the block. Here the last use of `parts` comes after the mutation. Move it before:

```rust
let mut url = String::from("https://example.com/docs");
let parts = Url::parse(&url);
println!("host {}", parts.host());
url.push_str("/intro");
```

This compiles with no copy at all. Reordering cannot help when the borrowed data really must outlive its source. Here the URL is moved into a history list while its host is still wanted:

```rust
pub fn visit(history: &mut Vec<String>) {
    let url = String::from("https://example.com/docs");
    let host = Url::parse(&url).host();
    history.push(url);
    println!("left {host}");
}
```

```
error[E0505]: cannot move out of `url` because it is borrowed
36 |     let host = Url::parse(&url).host();
   |                           ---- borrow of `url` occurs here
37 |     history.push(url);
   |                  ^^^ move out of `url` occurs here
38 |     println!("left {host}");
   |                     ---- borrow later used here
help: consider cloning the value if the performance cost is acceptable
36 |     let host = Url::parse(&url.clone()).host();
```

Taking that help literally fails again: the clone is a temporary, dropped at the end of the line, and `host` still points into it (`error[E0716]: temporary value dropped while borrowed`). Own the small part that must survive, not the whole URL:

```rust
    let host = Url::parse(&url).host().to_owned();
```

`host` is now a `String` of its own, and `url` is free to move. (`Url::parse(&url).host()` works even though the `Url` value is dropped on that same line, because `host` returns `&'a str`, which borrows the URL and not the struct.)

Predict: `Url::parse(&url)` comes first, then `url.push_str(...)`, then `parts.host()` is printed. Does it compile? And if the print moves above the `push_str`?
