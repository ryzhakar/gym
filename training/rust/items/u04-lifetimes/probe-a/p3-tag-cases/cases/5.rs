pub fn hand_off() -> usize {
    let name = String::from("ada");
    let view = &name;
    let moved = name;
    view.len() + moved.len()
}
