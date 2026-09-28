#![allow(dead_code)]

// Source checks for the structural rules in spec.md. Comments, string literals and
// char literals are skipped, so only real code counts.

/// The source with comments, string literals and char literals blanked out.
fn code_only(src: &str) -> String {
    let chars: Vec<char> = src.chars().collect();
    let mut out = String::new();
    let mut i = 0;
    while i < chars.len() {
        let c = chars[i];
        if c == '/' && chars.get(i + 1) == Some(&'/') {
            while i < chars.len() && chars[i] != '\n' {
                i += 1;
            }
        } else if c == '"' {
            i += 1;
            while i < chars.len() && chars[i] != '"' {
                if chars[i] == '\\' {
                    i += 1;
                }
                i += 1;
            }
            i += 1;
            out.push_str("\"\"");
        } else if c == '\'' && chars.get(i + 1) == Some(&'\\') {
            i += 4;
            out.push_str("' '");
        } else if c == '\'' && chars.get(i + 2) == Some(&'\'') {
            i += 3;
            out.push_str("' '");
        } else {
            out.push(c);
            i += 1;
        }
    }
    out
}

fn words(code: &str) -> Vec<&str> {
    code.split(|c: char| !(c.is_alphanumeric() || c == '_')).filter(|w| !w.is_empty()).collect()
}

/// How often `word` occurs as a whole token in the code.
pub fn count_word(src: &str, word: &str) -> usize {
    let code = code_only(src);
    words(&code).iter().filter(|w| **w == word).count()
}

fn is_word_at(chars: &[char], i: usize, word: &str) -> bool {
    let w: Vec<char> = word.chars().collect();
    let ident = |c: &char| c.is_alphanumeric() || *c == '_';
    chars.len() >= i + w.len()
        && chars[i..i + w.len()] == w[..]
        && (i == 0 || !ident(&chars[i - 1]))
        && chars.get(i + w.len()).map_or(true, |c| !ident(c))
}

/// The pattern of every arm of every `match`, guard included, trimmed.
pub fn arm_patterns(src: &str) -> Vec<String> {
    let chars: Vec<char> = code_only(src).chars().collect();
    let mut arms = Vec::new();
    let mut i = 0;
    while i < chars.len() {
        if !is_word_at(&chars, i, "match") {
            i += 1;
            continue;
        }
        // Find the `{` that opens the arms: the first one outside the scrutinee's brackets.
        let mut j = i + 5;
        let mut depth = 0i32;
        while j < chars.len() && !(chars[j] == '{' && depth == 0) {
            match chars[j] {
                '(' | '[' => depth += 1,
                ')' | ']' => depth -= 1,
                _ => {}
            }
            j += 1;
        }
        j += 1;
        let mut depth = 1i32;
        let mut pattern = String::new();
        let mut in_body = false;
        let mut block_body = false;
        while j < chars.len() && depth > 0 {
            let c = chars[j];
            if !in_body {
                if depth == 1 && c == '=' && chars.get(j + 1) == Some(&'>') {
                    arms.push(pattern.trim().to_string());
                    pattern.clear();
                    in_body = true;
                    j += 2;
                    while j < chars.len() && chars[j].is_whitespace() {
                        j += 1;
                    }
                    block_body = chars.get(j) == Some(&'{');
                    continue;
                }
                match c {
                    '(' | '[' | '{' => depth += 1,
                    ')' | ']' | '}' => depth -= 1,
                    _ => {}
                }
                if depth > 0 {
                    pattern.push(c);
                }
            } else {
                match c {
                    '(' | '[' | '{' => depth += 1,
                    ')' | ']' | '}' => depth -= 1,
                    _ => {}
                }
                let arm_done = (c == ',' && depth == 1) || (block_body && c == '}' && depth == 1);
                if arm_done {
                    in_body = false;
                    if block_body && chars.get(j + 1) == Some(&',') {
                        j += 1;
                    }
                }
            }
            j += 1;
        }
        i += 5;
    }
    arms
}

/// Arm alternatives that do not name a variant: `_`, a bare binding, or anything that does not start with a type or path.
pub fn arms_not_naming_a_variant(src: &str) -> Vec<String> {
    let mut bad = Vec::new();
    for arm in arm_patterns(src) {
        let chars: Vec<char> = arm.chars().collect();
        // Cut the guard: an `if` token outside brackets.
        let mut depth = 0i32;
        let mut end = chars.len();
        let mut starts = vec![0];
        for k in 0..chars.len() {
            match chars[k] {
                '(' | '[' | '{' => depth += 1,
                ')' | ']' | '}' => depth -= 1,
                '|' if depth == 0 => starts.push(k + 1),
                _ => {}
            }
            if depth == 0 && is_word_at(&chars, k, "if") {
                end = k;
                break;
            }
        }
        let pattern: String = chars[..end].iter().collect();
        let mut offsets: Vec<usize> = starts.into_iter().filter(|s| *s <= end).collect();
        offsets.push(end + 1);
        for w in offsets.windows(2) {
            let alt: String = pattern.chars().skip(w[0]).take(w[1] - 1 - w[0]).collect();
            let alt = alt.trim().to_string();
            let head: String = alt.chars().take_while(|c| !"({ ".contains(*c)).collect();
            let names_type = alt.chars().next().map_or(false, |c| c.is_ascii_uppercase()) || head.contains("::");
            if !names_type {
                bad.push(alt);
            }
        }
    }
    bad
}

const SRC: &str = include_str!("../src/lib.rs");

#[test]
fn every_arm_names_a_variant() {
    let bad = arms_not_naming_a_variant(SRC);
    assert!(bad.is_empty(), "arms that do not name a variant: {bad:?}");
}
