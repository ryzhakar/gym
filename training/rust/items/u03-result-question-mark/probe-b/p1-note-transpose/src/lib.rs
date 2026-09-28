use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum PitchError {
    MissingPrefix,
    BadNumber(ParseIntError),
    OutOfRange,
}

#[derive(Debug, PartialEq)]
pub struct Pitch {
    pub written: u8,
    pub sounding: u8,
}

/// Reads a note such as "N60" and moves it by `semitones`.
pub fn transpose(text: &str, semitones: i8) -> Result<Pitch, PitchError> {
    todo!()
}
