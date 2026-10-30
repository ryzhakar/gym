pub fn grow_log(log: &mut Vec<String>) -> usize {
    let first = &log[0];
    log.push(String::from("next"));
    first.len()
}
