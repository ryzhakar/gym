use u04_probe_a_p2::Row;

#[test]
fn empty_fields_count() {
    let mut row = Row::new("a,,b,");
    assert_eq!(row.next_field(), Some("a"));
    assert_eq!(row.next_field(), Some(""));
    assert_eq!(row.next_field(), Some("b"));
    assert_eq!(row.next_field(), Some(""));
    assert_eq!(row.next_field(), None);
}

#[test]
fn the_empty_line_is_one_empty_field() {
    let mut row = Row::new("");
    assert_eq!(row.next_field(), Some(""));
    assert_eq!(row.next_field(), None);
}

#[test]
fn none_on_every_later_call() {
    let mut row = Row::new("x");
    assert_eq!(row.next_field(), Some("x"));
    assert_eq!(row.next_field(), None);
    assert_eq!(row.next_field(), None);
    assert_eq!(row.next_field(), None);
}

#[test]
fn fields_keep_their_spaces() {
    let mut row = Row::new(" a , b");
    assert_eq!(row.next_field(), Some(" a "));
    assert_eq!(row.next_field(), Some(" b"));
}

#[test]
fn fields_outlive_a_moved_row() {
    let line = String::from("p,q,r");
    let fields: Vec<&str>;
    {
        let row = Row::new(&line);
        let mut moved = row;
        let mut got = Vec::new();
        while let Some(field) = moved.next_field() {
            got.push(field);
        }
        drop(moved);
        fields = got;
    }
    assert_eq!(fields, ["p", "q", "r"]);
}
