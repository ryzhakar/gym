// Source check for the rule in spec.md. Comments, string literals and char literals
// are skipped, so only real code counts.

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

/// How often `word` occurs as a whole token in the code.
fn count_word(src: &str, word: &str) -> usize {
    let code = code_only(src);
    code.split(|c: char| !(c.is_alphanumeric() || c == '_')).filter(|w| *w == word).count()
}

const SRC: &str = include_str!("../src/lib.rs");

#[test]
fn nothing_is_copied_into_an_owned_string() {
    for banned in ["String", "clone", "to_string", "to_owned", "Box"] {
        let n = count_word(SRC, banned);
        assert_eq!(n, 0, "src/lib.rs uses `{banned}` {n} time(s)");
    }
}
