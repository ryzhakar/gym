use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum DoseError {
    /// The dose text is not a `u32`.
    BadAmount(ParseIntError),
    /// The dose is 0.
    Empty,
    /// The dose is more than the stock.
    TooMuch { stock: u32, dose: u32 },
}

/// The stock left after taking out `dose_text`.
pub fn administer(stock: u32, dose_text: &str) -> Result<u32, DoseError> {
    let dose = dose_text.parse::<u32>().map_err(DoseError::BadAmount)?;
    if dose == 0 {
        return Err(DoseError::Empty);
    }
    let left = stock.checked_sub(dose).ok_or(DoseError::TooMuch { stock, dose })?;
    Ok(left)
}
