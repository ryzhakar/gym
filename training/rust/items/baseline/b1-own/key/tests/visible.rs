use b1_own::keep_long;

fn owned(words: &[&str]) -> Vec<String> {
    words.iter().map(|w| w.to_string()).collect()
}

#[test]
fn counts_all_and_keeps_long() {
    let (total, kept) = keep_long(owned(&["a", "abcde", "xyz", "hello!"]), 3);
    assert_eq!(total, 4);
    assert_eq!(kept, owned(&["abcde", "hello!"]));
}
