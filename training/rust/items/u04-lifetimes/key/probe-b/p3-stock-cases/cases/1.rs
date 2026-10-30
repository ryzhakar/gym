pub fn lowest_two(counts: &[u32]) -> &[u32] {
    let mut sorted = counts.to_vec();
    sorted.sort();
    &sorted[..2]
}
