pub fn rename(names: &mut Vec<String>) {
    let first = &mut names[0];
    let last = &mut names[1];
    first.push_str("!");
    last.push_str("?");
}
