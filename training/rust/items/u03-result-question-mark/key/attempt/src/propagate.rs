//! With the question-mark operator for every failure.

use crate::LineError;

pub fn parse_line(line: &str) -> Result<(&str, u32), LineError> {
    let (name, count) = line.split_once('=').ok_or(LineError::NoEquals)?;
    if name.is_empty() {
        return Err(LineError::EmptyName);
    }
    let count = count.parse::<u32>().map_err(LineError::BadCount)?;
    Ok((name, count))
}
