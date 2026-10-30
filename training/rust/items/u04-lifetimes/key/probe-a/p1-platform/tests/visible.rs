use u04_probe_a_p1::{next_stop, platform};

#[test]
fn next_stop_follows_the_route() {
    let found: &str = next_stop("Ash Birch Cedar", "Birch");
    assert_eq!(found, "Cedar");
}

#[test]
fn next_stop_stays_put_at_the_end_or_off_the_route() {
    assert_eq!(next_stop("Ash Birch", "Birch"), "Birch");
    assert_eq!(next_stop("Ash Birch", "Oak"), "Oak");
}

#[test]
fn platform_outlives_the_stop_name() {
    let board = String::from("Ash=2\nBirch=5");
    let found: &str;
    {
        let stop = String::from("Birch");
        found = platform(&board, &stop, "none");
    }
    assert_eq!(found, "5");
}

#[test]
fn platform_falls_back() {
    let found: &str = platform("Ash=2", "Oak", "none");
    assert_eq!(found, "none");
}
