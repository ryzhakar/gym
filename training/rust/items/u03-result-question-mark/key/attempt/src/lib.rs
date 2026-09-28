//! Config lines, parsed twice. See attempt.md.

use std::num::ParseIntError;

pub mod explicit;
pub mod propagate;

#[derive(Debug, PartialEq)]
pub enum LineError {
    /// The line has no `=`.
    NoEquals,
    /// Nothing before the first `=`.
    EmptyName,
    /// The part after the first `=` is not a `u32`.
    BadCount(ParseIntError),
}
