/// Returns how many words there were, and the words longer than `min` bytes, in their original order.
pub fn keep_long(words: Vec<String>, min: usize) -> (usize, Vec<String>) {
    let total = words.len();
    let mut kept = Vec::new();
    for w in words {
        if w.len() > min {
            kept.push(w);
        }
    }
    (total, kept)
}
