pub trait Area {
    fn area(&self) -> f64;
}

pub struct Rect {
    pub w: f64,
    pub h: f64,
}

pub struct Square(pub f64);

// Implement `Area` for `Rect` and `Square`, and write `total_area`. See spec.md.
