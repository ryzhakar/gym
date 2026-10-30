pub fn retire_first(items: &mut Vec<String>) {
    let first = &items[0];
    let renamed = format!("{first}-old");
    items[0] = renamed;
}
