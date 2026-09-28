use u01_unshown::Inbox;

#[test]
fn hands_over_the_original_messages() {
    let mut inbox = Inbox { pending: vec!["one".to_string(), "two".to_string()], done: 3 };
    let addrs: Vec<*const u8> = inbox.pending.iter().map(|m| m.as_ptr()).collect();
    let got = inbox.drain_all();
    assert_eq!(got, vec!["one", "two"]);
    assert_eq!(got.iter().map(|m| m.as_ptr()).collect::<Vec<_>>(), addrs);
    assert!(inbox.pending.is_empty());
    assert_eq!(inbox.done, 5);
}
