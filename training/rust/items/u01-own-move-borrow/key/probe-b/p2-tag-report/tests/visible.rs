use u01_probe_b_p2::report;

fn tags(words: &[&str]) -> Vec<String> {
    words.iter().map(|w| w.to_string()).collect()
}

#[test]
fn counts_urgent_tags_and_all_tags() {
    let r = report(tags(&["urgent", "billing", "urgent"]));
    assert_eq!(r.urgent, 2);
    assert_eq!(r.total, 3);
}
