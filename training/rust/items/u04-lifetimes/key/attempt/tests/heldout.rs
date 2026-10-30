use u04_attempt::{first_reading, number_of, prefer_unit};

#[test]
fn signatures_borrow_only_where_the_result_comes_from() {
    let _: for<'a, 'b> fn(&'a str, &'b str) -> &'a str = number_of;
    let _: for<'a> fn(&'a str, &'a str) -> &'a str = first_reading;
    let _: for<'a, 'b> fn(&'a str, &'a str, &'b str) -> &'a str = prefer_unit;
}

#[test]
fn number_points_into_the_reading() {
    let reading = String::from("9.75mm");
    let number = number_of(&reading, "mm");
    assert_eq!(number, "9.75");
    assert_eq!(number.as_ptr(), reading.as_ptr());
}

#[test]
fn reading_that_is_only_the_unit() {
    assert_eq!(number_of("kg", "kg"), "");
}

#[test]
fn unit_in_the_middle_is_not_cut() {
    assert_eq!(number_of("2kg3", "kg"), "2kg3");
}

#[test]
fn first_reading_points_into_the_input_it_returns() {
    let log = String::from("1kg\n2kg");
    let fallback = String::from("none");
    let first = first_reading(&log, &fallback);
    assert_eq!(first, "1kg");
    assert_eq!(first.as_ptr(), log.as_ptr());
    let empty = String::new();
    let chosen = first_reading(&empty, &fallback);
    assert_eq!(chosen.as_ptr(), fallback.as_ptr());
}

#[test]
fn first_line_of_a_one_line_log() {
    assert_eq!(first_reading("5kg", "none"), "5kg");
}

#[test]
fn choice_points_into_a_or_b() {
    let a = String::from("1kg");
    let b = String::from("2lb");
    assert_eq!(prefer_unit(&a, &b, "kg").as_ptr(), a.as_ptr());
    assert_eq!(prefer_unit(&a, &b, "lb").as_ptr(), b.as_ptr());
}

#[test]
fn choice_outlives_a_unit_built_on_the_spot() {
    let a = String::from("3lb");
    let b = String::from("4kg");
    let choice = prefer_unit(&a, &b, &String::from("kg"));
    assert_eq!(choice, "4kg");
}
