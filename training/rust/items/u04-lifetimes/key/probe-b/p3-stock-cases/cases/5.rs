pub fn ship_crate() -> usize {
    let label = String::from("crate-7");
    let code = &label[..5];
    let shipped = vec![label];
    code.len() + shipped.len()
}
