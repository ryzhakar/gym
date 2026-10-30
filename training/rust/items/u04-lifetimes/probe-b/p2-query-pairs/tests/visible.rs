use u04_probe_b_p2::Pairs;

#[test]
fn pairs_in_order_then_none() {
    let mut pairs = Pairs::new("size=9;color=red");
    assert_eq!(pairs.next_pair(), Some(("size", "9")));
    assert_eq!(pairs.next_pair(), Some(("color", "red")));
    assert_eq!(pairs.next_pair(), None);
}

#[test]
fn pairs_outlive_the_reader() {
    let query = String::from("page=2;sort=asc");
    let first: Option<(&str, &str)>;
    let second: Option<(&str, &str)>;
    {
        let mut pairs = Pairs::new(&query);
        first = pairs.next_pair();
        second = pairs.next_pair();
    }
    assert_eq!(first, Some(("page", "2")));
    assert_eq!(second, Some(("sort", "asc")));
}
