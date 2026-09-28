use u01_unshown::Inbox;

#[test]
fn signature_is_unchanged() {
    let _: fn(&mut Inbox) -> Vec<String> = Inbox::drain_all;
}

#[test]
fn second_drain_is_empty() {
    let mut inbox = Inbox { pending: vec!["a".to_string()], done: 0 };
    inbox.drain_all();
    assert!(inbox.drain_all().is_empty());
    assert_eq!(inbox.done, 1);
}

#[test]
fn inbox_is_usable_after() {
    let mut inbox = Inbox { pending: vec!["a".to_string()], done: 0 };
    inbox.drain_all();
    inbox.pending.push("b".to_string());
    assert_eq!(inbox.drain_all(), vec!["b"]);
    assert_eq!(inbox.done, 2);
}

#[test]
fn no_copies() {
    let src = include_str!("../src/lib.rs");
    for banned in ["clone", "to_owned", "to_vec", "to_string"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}
