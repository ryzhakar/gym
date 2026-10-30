use u04_probe_b_p2::Pairs;

#[test]
fn a_piece_without_equals_is_all_key() {
    let mut pairs = Pairs::new("debug;level=3");
    assert_eq!(pairs.next_pair(), Some(("debug", "")));
    assert_eq!(pairs.next_pair(), Some(("level", "3")));
    assert_eq!(pairs.next_pair(), None);
}

#[test]
fn split_at_the_first_equals() {
    let mut pairs = Pairs::new("expr=a=b;k=");
    assert_eq!(pairs.next_pair(), Some(("expr", "a=b")));
    assert_eq!(pairs.next_pair(), Some(("k", "")));
    assert_eq!(pairs.next_pair(), None);
}

#[test]
fn empty_pieces_are_skipped() {
    let mut pairs = Pairs::new(";a=1;;b=2;");
    assert_eq!(pairs.next_pair(), Some(("a", "1")));
    assert_eq!(pairs.next_pair(), Some(("b", "2")));
    assert_eq!(pairs.next_pair(), None);
    assert_eq!(Pairs::new(";;").next_pair(), None);
}

#[test]
fn a_lone_equals_is_not_empty() {
    let mut pairs = Pairs::new("=;x");
    assert_eq!(pairs.next_pair(), Some(("", "")));
    assert_eq!(pairs.next_pair(), Some(("x", "")));
    assert_eq!(pairs.next_pair(), None);
}

#[test]
fn the_empty_query_has_no_pairs_and_none_repeats() {
    let mut pairs = Pairs::new("");
    assert_eq!(pairs.next_pair(), None);
    assert_eq!(pairs.next_pair(), None);
    let mut one = Pairs::new("x=1");
    assert_eq!(one.next_pair(), Some(("x", "1")));
    assert_eq!(one.next_pair(), None);
    assert_eq!(one.next_pair(), None);
}

#[test]
fn pairs_outlive_a_moved_reader() {
    let query = String::from("p=1;q=2;r=3");
    let keys: Vec<&str>;
    {
        let pairs = Pairs::new(&query);
        let mut moved = pairs;
        let mut got = Vec::new();
        while let Some((key, _)) = moved.next_pair() {
            got.push(key);
        }
        drop(moved);
        keys = got;
    }
    assert_eq!(keys, ["p", "q", "r"]);
}
