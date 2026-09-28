pub struct TagReport {
    pub urgent: usize,
    pub total: usize,
}

fn count_matching(tags: &[String], wanted: &str) -> usize {
    let mut n = 0;
    for tag in tags.iter() {
        if tag == wanted {
            n += 1;
        }
    }
    n
}

/// Counts the tags equal to "urgent", and all tags.
pub fn report(tags: Vec<String>) -> TagReport {
    let urgent = count_matching(&tags, "urgent");
    TagReport { urgent, total: tags.len() }
}
