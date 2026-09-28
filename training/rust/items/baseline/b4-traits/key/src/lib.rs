pub trait Area {
    fn area(&self) -> f64;
}

pub struct Rect {
    pub w: f64,
    pub h: f64,
}

pub struct Square(pub f64);

impl Area for Rect {
    fn area(&self) -> f64 {
        self.w * self.h
    }
}

impl Area for Square {
    fn area(&self) -> f64 {
        self.0 * self.0
    }
}

pub fn total_area<T: Area>(shapes: &[T]) -> f64 {
    let mut sum = 0.0;
    for s in shapes {
        sum += s.area();
    }
    sum
}
