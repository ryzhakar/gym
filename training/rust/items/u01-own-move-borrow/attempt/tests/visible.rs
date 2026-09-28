use u01_attempt::{callee_side, caller_side, drop_shorter_than_first};

fn owned(words: &[&str]) -> Vec<String> {
    words.iter().map(|w| w.to_string()).collect()
}

#[test]
fn drops_shorter_names_in_place() {
    let mut roster = owned(&["abc", "a", "abcd", "ab", "xyz"]);
    let before: Vec<*const u8> = roster.iter().map(|n| n.as_ptr()).collect();
    assert_eq!(drop_shorter_than_first(&mut roster), 3);
    assert_eq!(roster, owned(&["abc", "abcd", "xyz"]));
    let after: Vec<*const u8> = roster.iter().map(|n| n.as_ptr()).collect();
    assert_eq!(after, vec![before[0], before[2], before[4]]);
}

#[test]
fn caller_side_report() {
    assert_eq!(caller_side::a_report(owned(&["ann", "bob", "amy"])), "2/3");
}

#[test]
fn caller_side_keeps_count_starting_as_written() {
    let _: fn(Vec<String>, char) -> usize = caller_side::count_starting;
}

#[test]
fn callee_side_report() {
    assert_eq!(callee_side::a_report(owned(&["ann", "bob", "amy", "al"])), "3/4");
}

#[test]
fn callee_side_count_starting_leaves_names_usable() {
    let names = owned(&["ann", "bob"]);
    assert_eq!(callee_side::count_starting(&names, 'b'), 1);
    assert_eq!(names.len(), 2);
}

#[test]
fn no_string_copies_in_src() {
    let sources = [
        include_str!("../src/lib.rs"),
        include_str!("../src/caller_side.rs"),
        include_str!("../src/callee_side.rs"),
    ];
    for src in sources {
        for banned in ["clone", "to_owned", "to_vec", "to_string"] {
            assert!(!src.contains(banned), "src contains `{banned}`");
        }
    }
}
