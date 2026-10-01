/// `"none"`, `"right <n>"`, `"level"` or `"left <n>"`.
pub fn tilt_status(x: Option<i32>) -> String {
    match x {
        None => "none".to_string(),
        Some(n) if n > 0 => format!("right {n}"),
        Some(n) if n < 0 => format!("left {n}"),
        Some(_) => "level".to_string(),
    }
}
