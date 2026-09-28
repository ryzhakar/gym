//! Without the question-mark operator: a test rejects this file if that character appears in it, comments included.

use crate::LineError;

pub fn parse_line(line: &str) -> Result<(&str, u32), LineError> {
    let (name, count) = match line.split_once('=') {
        Some(parts) => parts,
        None => return Err(LineError::NoEquals),
    };
    if name.is_empty() {
        return Err(LineError::EmptyName);
    }
    match count.parse::<u32>() {
        Ok(n) => Ok((name, n)),
        Err(e) => Err(LineError::BadCount(e)),
    }
}
