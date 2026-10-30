use u04_reuse_3::{append, finish};

#[test]
fn append_to_an_empty_log() {
    let mut log = Vec::new();
    assert_eq!(append(&mut log, String::from("boot")), 0);
    assert_eq!(log, ["boot"]);
}

#[test]
fn append_reports_the_previous_line() {
    let mut log = vec![String::from("boot"), String::from("ready")];
    assert_eq!(append(&mut log, String::from("go")), 5);
    assert_eq!(log, ["boot", "ready", "go"]);
}

#[test]
fn finish_marks_and_adds() {
    let mut entries = vec![String::from("wash"), String::from("dry")];
    assert_eq!(finish(&mut entries, 0, String::from("fold")), 3);
    assert_eq!(entries, ["wash (done)", "dry", "fold"]);
}
