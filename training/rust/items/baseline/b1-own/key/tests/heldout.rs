use b1_own::keep_long;

#[test]
fn signature_is_unchanged() {
    let _: fn(Vec<String>, usize) -> (usize, Vec<String>) = keep_long;
}

#[test]
fn kept_strings_are_the_originals() {
    let words = vec!["tiny".to_string(), "lengthy".to_string(), "ok".to_string(), "sizeable".to_string()];
    let addrs: Vec<*const u8> = words.iter().map(|w| w.as_ptr()).collect();
    let (total, kept) = keep_long(words, 4);
    assert_eq!(total, 4);
    assert_eq!(kept.len(), 2);
    assert_eq!(kept[0].as_ptr(), addrs[1]);
    assert_eq!(kept[1].as_ptr(), addrs[3]);
}

#[test]
fn nothing_kept_is_still_counted() {
    let (total, kept) = keep_long(vec!["ab".to_string(), "cd".to_string()], 5);
    assert_eq!(total, 2);
    assert!(kept.is_empty());
}

#[test]
fn empty_input() {
    assert_eq!(keep_long(Vec::new(), 0), (0, Vec::new()));
}
