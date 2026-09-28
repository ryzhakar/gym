/// Adds `bonus` to every score strictly below the highest score.
/// Returns the highest score, or 0 when there are no scores.
pub fn lift_below_top(scores: &mut Vec<u32>, bonus: u32) -> u32 {
    let top = *scores.iter().max().unwrap_or(&0);
    for s in scores.iter_mut() {
        if *s < top {
            *s += bonus;
        }
    }
    top
}
