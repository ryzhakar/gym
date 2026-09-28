use u03_probe_a_p2::{area, SizeError};

fn int_error(text: &str) -> std::num::ParseIntError {
    match text.parse::<u32>() {
        Err(e) => e,
        Ok(n) => panic!("test setup: {text} parsed as {n}"),
    }
}

#[test]
fn area_of_a_size() {
    assert_eq!(area("3x4"), Ok(12));
}

#[test]
fn every_failure_is_told_apart() {
    assert_eq!(area("34"), Err(SizeError::MissingX));
    assert_eq!(area("ax4"), Err(SizeError::BadWidth(int_error("a"))));
    assert_eq!(area("3xb"), Err(SizeError::BadHeight(int_error("b"))));
}
