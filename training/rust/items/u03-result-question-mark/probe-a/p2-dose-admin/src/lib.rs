#[derive(Debug, PartialEq)]
pub enum DoseError {
    /// No dose is listed for the drug.
    UnknownDrug,
    /// The listed dose is 0.
    Empty,
    /// The dose is more than the stock.
    TooMuch { stock: u32, dose: u32 },
}

/// The stock left after one dose of `drug`, its dose looked up in `doses`.
pub fn administer(stock: u32, drug: &str, doses: &[(&str, u32)]) -> Result<u32, DoseError> {
    let &(_, dose) = doses.iter().find(|(name, _)| *name == drug)?;
    if dose == 0 {
        return Err(DoseError::Empty);
    }
    Ok(stock - dose)
}
