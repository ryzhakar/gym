use u01_probe_b_p2::{report, TagReport};

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

fn tags(words: &[&str]) -> Vec<String> {
    words.iter().map(|w| w.to_string()).collect()
}

#[test]
fn signature_is_kept() {
    let _: fn(Vec<String>) -> TagReport = report;
}

#[test]
fn empty_list() {
    let r = report(Vec::new());
    assert_eq!(r.urgent, 0);
    assert_eq!(r.total, 0);
}

#[test]
fn single_tag_that_is_not_urgent() {
    let r = report(tags(&["ops"]));
    assert_eq!(r.urgent, 0);
    assert_eq!(r.total, 1);
}

#[test]
fn many_tags_match_exactly() {
    let r = report(tags(&["Urgent", "urgent", "ops", "urgent ", "urgent", "", "urgent"]));
    assert_eq!(r.urgent, 3);
    assert_eq!(r.total, 7);
}

#[test]
fn tags_are_not_copied() {
    let code = code();
    for banned in [
        "clone", "to_owned", "to_vec", "to_string", "collect", "String::from", "format!", ".into(",
    ] {
        assert!(!code.contains(banned), "src/lib.rs uses `{banned}`");
    }
}
