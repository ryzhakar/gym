use u04_probe_a_p2::Row;

#[test]
fn fields_in_order_then_none() {
    let mut row = Row::new("ash,birch,cedar");
    assert_eq!(row.next_field(), Some("ash"));
    assert_eq!(row.next_field(), Some("birch"));
    assert_eq!(row.next_field(), Some("cedar"));
    assert_eq!(row.next_field(), None);
}

#[test]
fn fields_outlive_the_row() {
    let line = String::from("12,oak");
    let first: Option<&str>;
    let second: Option<&str>;
    {
        let mut row = Row::new(&line);
        first = row.next_field();
        second = row.next_field();
    }
    assert_eq!(first, Some("12"));
    assert_eq!(second, Some("oak"));
}

#[test]
fn a_trailing_comma_ends_with_an_empty_field() {
    let mut row = Row::new("elm,");
    assert_eq!(row.next_field(), Some("elm"));
    assert_eq!(row.next_field(), Some(""));
    assert_eq!(row.next_field(), None);
}
