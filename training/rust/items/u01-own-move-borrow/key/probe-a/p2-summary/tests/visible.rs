use u01_probe_a_p2::summary;

#[test]
fn counts_lines_and_bytes() {
    let lines = vec!["ab".to_string(), "cde".to_string()];
    assert_eq!(summary(lines), "2 lines, 5 bytes");
}
