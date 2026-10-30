// Source check for the rule in spec.md. Comments and string literals are skipped, so only real code counts.

/// The source with `//` comments and string literals blanked out.
fn code_only(src: &str) -> String {
    let mut out = String::new();
    for line in src.lines() {
        let mut in_string = false;
        let mut chars = line.chars().peekable();
        while let Some(c) = chars.next() {
            if in_string {
                if c == '\\' {
                    chars.next();
                } else if c == '"' {
                    in_string = false;
                    out.push('"');
                }
            } else if c == '"' {
                in_string = true;
                out.push('"');
            } else if c == '/' && chars.peek() == Some(&'/') {
                break;
            } else {
                out.push(c);
            }
        }
        out.push('\n');
    }
    out
}

#[test]
fn no_copy_of_a_string() {
    let code: String = code_only(include_str!("../src/lib.rs")).split_whitespace().collect();
    for banned in [".clone()", ".cloned()", "to_owned", "to_string", "String::from"] {
        assert!(!code.contains(banned), "src/lib.rs contains `{banned}`");
    }
}
