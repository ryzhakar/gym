use u04_reuse_3::{append, finish};

#[test]
fn signatures_are_unchanged() {
    let _: fn(&mut Vec<String>, String) -> usize = append;
    let _: fn(&mut Vec<String>, usize, String) -> usize = finish;
}

#[test]
fn append_counts_bytes_of_the_old_last_line_only() {
    let mut log = vec![String::from("a"), String::from("")];
    assert_eq!(append(&mut log, String::from("longer line")), 0);
    assert_eq!(append(&mut log, String::from("x")), 11);
    assert_eq!(log, ["a", "", "longer line", "x"]);
}

#[test]
fn finish_the_last_entry() {
    let mut entries = vec![String::from("plan")];
    assert_eq!(finish(&mut entries, 0, String::from("build")), 2);
    assert_eq!(finish(&mut entries, 1, String::from("ship")), 3);
    assert_eq!(entries, ["plan (done)", "build (done)", "ship"]);
}

#[test]
fn finish_leaves_other_entries() {
    let mut entries = vec![String::from("a"), String::from("b"), String::from("c")];
    assert_eq!(finish(&mut entries, 2, String::from("d")), 4);
    assert_eq!(entries, ["a", "b", "c (done)", "d"]);
}
