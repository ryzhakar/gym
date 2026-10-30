use u04_probe_a_p1::{next_stop, platform};

#[test]
fn next_stop_borrows_from_an_owned_route() {
    let route = String::from("Ash Birch Cedar Dune");
    let from = String::from("Cedar");
    let found: &str = next_stop(&route, &from);
    assert_eq!(found, "Dune");
    assert_eq!(next_stop(&route, "Ash"), "Birch");
}

#[test]
fn next_stop_returns_the_given_stop_when_off_the_route() {
    let route = String::from("Ash Birch");
    let from = String::from("Elm");
    let found: &str = next_stop(&route, &from);
    assert_eq!(found, "Elm");
    assert_eq!(next_stop("", "Elm"), "Elm");
}

#[test]
fn platform_outlives_the_stop_name_with_an_owned_fallback() {
    let board = String::from("Ash=2");
    let fallback = String::from("?");
    let found: &str;
    {
        let stop = String::from("Zed");
        found = platform(&board, &stop, &fallback);
    }
    assert_eq!(found, "?");
}

#[test]
fn platform_takes_the_first_matching_line_and_skips_lines_without_equals() {
    let board = "Ash\nBirch=5\nBirch=9\nCedar=";
    assert_eq!(platform(board, "Birch", "none"), "5");
    assert_eq!(platform(board, "Ash", "none"), "none");
    assert_eq!(platform(board, "Cedar", "none"), "");
}
