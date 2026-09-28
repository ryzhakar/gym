/// `"none"`, `"positive <n>"`, `"zero"` or `"negative <n>"`.
pub fn sign_of(x: Option<i32>) -> String {
    match x {
        None => "none".to_string(),
        Some(n) if n > 0 => format!("positive {n}"),
        Some(n) if n == 0 => "zero".to_string(),
        Some(n) if n < 0 => format!("negative {n}"),
    }
}
