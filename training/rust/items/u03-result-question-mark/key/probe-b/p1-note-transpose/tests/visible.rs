use std::num::ParseIntError;
use u03_probe_b_p1::{transpose, Pitch, PitchError};

fn u8_error(text: &str) -> ParseIntError {
    match text.parse::<u8>() {
        Err(e) => e,
        Ok(_) => panic!("{text:?} parses"),
    }
}

#[test]
fn moves_a_note_up_and_down() {
    assert_eq!(transpose("N60", 7), Ok(Pitch { written: 60, sounding: 67 }));
    assert_eq!(transpose("N60", -12), Ok(Pitch { written: 60, sounding: 48 }));
}

#[test]
fn missing_prefix() {
    assert_eq!(transpose("60", 0), Err(PitchError::MissingPrefix));
}

#[test]
fn bad_number() {
    assert_eq!(transpose("Nsix", 0), Err(PitchError::BadNumber(u8_error("six"))));
}

#[test]
fn out_of_range() {
    assert_eq!(transpose("N250", 10), Err(PitchError::OutOfRange));
}
