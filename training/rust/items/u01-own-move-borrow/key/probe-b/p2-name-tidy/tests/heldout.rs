use u01_probe_b_p2::{tidy, Tidy};

const SOURCE: &str = include_str!("../src/lib.rs");

fn code() -> String {
    SOURCE
        .lines()
        .map(|line| match line.find("//") {
            Some(at) => &line[..at],
            None => line,
        })
        .collect::<Vec<_>>()
        .join("\n")
}

fn names(words: &[&str]) -> Vec<String> {
    let mut out = Vec::new();
    for w in words {
        out.push(String::from(*w));
    }
    out
}

#[test]
fn signature_is_kept() {
    let _: fn(Vec<String>) -> Tidy = tidy;
}

#[test]
fn empty_list() {
    let t = tidy(Vec::new());
    assert_eq!(t.removed, 0);
    assert_eq!(t.last, None);
}

#[test]
fn single_name() {
    let t = tidy(names(&["kiwi"]));
    assert_eq!(t.removed, 0);
    assert_eq!(t.last.as_deref(), Some("kiwi"));
}

#[test]
fn all_the_same() {
    let t = tidy(names(&["lime", "lime", "lime"]));
    assert_eq!(t.removed, 2);
    assert_eq!(t.last.as_deref(), Some("lime"));
}

#[test]
fn last_input_is_not_the_last_name() {
    let t = tidy(names(&["plum", "date", "plum", "yuzu", "date", "cherry"]));
    assert_eq!(t.removed, 2);
    assert_eq!(t.last.as_deref(), Some("yuzu"));
}

#[test]
fn last_name_is_the_original_string() {
    let list = names(&["fig", "yuzu", "apple", "fig"]);
    let yuzu_at = list[1].as_ptr();
    let t = tidy(list);
    assert_eq!(t.removed, 1);
    assert_eq!(t.last.as_ref().map(|s| s.as_ptr()), Some(yuzu_at));
}

#[test]
fn surviving_repeat_is_the_first_one() {
    let list = names(&["oak", "elm", "oak"]);
    let first_oak = list[0].as_ptr();
    let t = tidy(list);
    assert_eq!(t.last.as_ref().map(|s| s.as_ptr()), Some(first_oak));
}

#[test]
fn names_are_not_copied() {
    let code = code();
    for banned in ["clone", "to_owned", "to_vec", "to_string"] {
        assert!(!code.contains(banned), "src/lib.rs uses `{banned}`");
    }
}
