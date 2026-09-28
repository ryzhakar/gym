use std::num::ParseIntError;
use u03_probe_b_p1::{transpose, Pitch, PitchError};

const SOURCE: &str = include_str!("../src/lib.rs");

fn code() -> String {
    SOURCE
        .lines()
        .map(|line| match line.find("//") {
            Some(at) => &line[..at],
            None => line,
        })
        .collect::<Vec<_>>()
        .join("\n")
}

#[test]
fn no_panic_on_input() {
    let code = code();
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!code.contains(banned), "src/lib.rs uses `{banned}`");
    }
}

fn u8_error(text: &str) -> ParseIntError {
    match text.parse::<u8>() {
        Err(e) => e,
        Ok(_) => panic!("{text:?} parses"),
    }
}

#[test]
fn signature_is_kept() {
    let _: fn(&str, i8) -> Result<Pitch, PitchError> = transpose;
}

#[test]
fn types_are_kept() {
    fn variants(e: PitchError) -> u8 {
        match e {
            PitchError::MissingPrefix => 0,
            PitchError::BadNumber(_) => 1,
            PitchError::OutOfRange => 2,
        }
    }
    assert_eq!(variants(PitchError::BadNumber(u8_error("x"))), 1);
    let Pitch { written, sounding } = Pitch { written: 1u8, sounding: 2u8 };
    assert_eq!((written, sounding), (1, 2));
}

#[test]
fn top_edge() {
    assert_eq!(transpose("N255", 0), Ok(Pitch { written: 255, sounding: 255 }));
    assert_eq!(transpose("N250", 5), Ok(Pitch { written: 250, sounding: 255 }));
    assert_eq!(transpose("N250", 6), Err(PitchError::OutOfRange));
    assert_eq!(transpose("N255", 1), Err(PitchError::OutOfRange));
    assert_eq!(transpose("N128", i8::MAX), Ok(Pitch { written: 128, sounding: 255 }));
    assert_eq!(transpose("N129", i8::MAX), Err(PitchError::OutOfRange));
}

#[test]
fn bottom_edge() {
    assert_eq!(transpose("N0", 0), Ok(Pitch { written: 0, sounding: 0 }));
    assert_eq!(transpose("N0", -1), Err(PitchError::OutOfRange));
    assert_eq!(transpose("N128", i8::MIN), Ok(Pitch { written: 128, sounding: 0 }));
    assert_eq!(transpose("N127", i8::MIN), Err(PitchError::OutOfRange));
}

#[test]
fn number_edges() {
    assert_eq!(transpose("N256", -1), Err(PitchError::BadNumber(u8_error("256"))));
    assert_eq!(transpose("N-1", 1), Err(PitchError::BadNumber(u8_error("-1"))));
}

#[test]
fn empty_input() {
    assert_eq!(transpose("", 0), Err(PitchError::MissingPrefix));
}

#[test]
fn prefix_alone() {
    assert_eq!(transpose("N", 0), Err(PitchError::BadNumber(u8_error(""))));
}

#[test]
fn prefix_elsewhere() {
    assert_eq!(transpose("60N", 0), Err(PitchError::MissingPrefix));
    assert_eq!(transpose("n60", 0), Err(PitchError::MissingPrefix));
    assert_eq!(transpose(" N60", 0), Err(PitchError::MissingPrefix));
}
