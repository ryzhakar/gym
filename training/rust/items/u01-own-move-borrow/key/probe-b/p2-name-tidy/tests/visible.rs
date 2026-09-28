use u01_probe_b_p2::tidy;

fn names(words: &[&str]) -> Vec<String> {
    let mut out = Vec::new();
    for w in words {
        out.push(String::from(*w));
    }
    out
}

#[test]
fn removes_repeats_and_reports_the_last_name() {
    let t = tidy(names(&["pear", "fig", "pear", "apple"]));
    assert_eq!(t.removed, 1);
    assert_eq!(t.last.as_deref(), Some("pear"));
}
