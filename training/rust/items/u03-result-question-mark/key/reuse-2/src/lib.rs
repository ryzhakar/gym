use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub enum TxError {
    /// The amount text is not a `u64`.
    BadAmount(ParseIntError),
    /// The amount is 0.
    Zero,
    /// The amount is more than the balance.
    Insufficient { balance: u64, amount: u64 },
}

/// The balance after taking out `amount_text`.
pub fn withdraw(balance: u64, amount_text: &str) -> Result<u64, TxError> {
    let amount = amount_text.parse::<u64>().map_err(TxError::BadAmount)?;
    if amount == 0 {
        return Err(TxError::Zero);
    }
    let left = balance.checked_sub(amount).ok_or(TxError::Insufficient { balance, amount })?;
    Ok(left)
}
