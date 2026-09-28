//! Roster helpers. See attempt.md.

pub mod callee_side;
pub mod caller_side;

/// Removes every name shorter than the first name and keeps the rest in order.
/// Returns the first name's byte length. Panics on an empty roster.
pub fn drop_shorter_than_first(roster: &mut Vec<String>) -> usize {
    let min = roster[0].len();
    roster.retain(|n| n.len() >= min);
    min
}
