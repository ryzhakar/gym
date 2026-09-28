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
    let digits = text.strip_prefix('N').ok_or(PitchError::MissingPrefix)?;
    let written: u8 = digits.parse().map_err(PitchError::BadNumber)?;
    let sounding = written.checked_add_signed(semitones).ok_or(PitchError::OutOfRange)?;
    Ok(Pitch { written, sounding })
}
