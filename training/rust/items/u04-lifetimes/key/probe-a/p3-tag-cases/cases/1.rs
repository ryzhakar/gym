pub fn tag_after_last(tags: &mut Vec<String>) {
    let last = tags.last();
    let note = match last {
        Some(tag) => format!("after {tag}"),
        None => String::from("first"),
    };
    tags.push(note);
}
