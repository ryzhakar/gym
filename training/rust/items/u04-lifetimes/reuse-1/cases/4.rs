pub fn greeting(name: &str) -> &str {
    let text = format!("hello, {name}");
    &text
}
