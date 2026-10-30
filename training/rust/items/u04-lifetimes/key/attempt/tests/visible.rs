use u04_attempt::{first_reading, number_of, prefer_unit};

#[test]
fn number_without_its_unit() {
    assert_eq!(number_of("12.5kg", "kg"), "12.5");
}

#[test]
fn reading_in_another_unit_comes_back_whole() {
    assert_eq!(number_of("12.5lb", "kg"), "12.5lb");
}

#[test]
fn number_outlives_the_unit() {
    let reading = String::from("40cm");
    let number;
    {
        let unit = String::from("cm");
        number = number_of(&reading, &unit);
    }
    assert_eq!(number, "40");
}

#[test]
fn first_line_of_the_log() {
    assert_eq!(first_reading("3kg\n4kg", "none"), "3kg");
}

#[test]
fn empty_log_gives_the_fallback() {
    assert_eq!(first_reading("", "none"), "none");
}

#[test]
fn prefers_the_reading_in_the_unit() {
    assert_eq!(prefer_unit("3kg", "7lb", "kg"), "3kg");
    assert_eq!(prefer_unit("7lb", "3kg", "kg"), "3kg");
}

#[test]
fn choice_outlives_the_unit() {
    let a = String::from("5lb");
    let b = String::from("2kg");
    let choice;
    {
        let unit = String::from("kg");
        choice = prefer_unit(&a, &b, &unit);
    }
    assert_eq!(choice, "2kg");
}
