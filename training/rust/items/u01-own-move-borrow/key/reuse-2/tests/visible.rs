use u01_reuse_2::broadcast;

#[test]
fn one_line_per_recipient() {
    let to = vec!["ann".to_string(), "bob".to_string()];
    assert_eq!(broadcast(&to, "lunch?".to_string()), vec!["ann: lunch?", "bob: lunch?"]);
    assert_eq!(to.len(), 2);
}
