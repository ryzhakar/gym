use b4_traits::{total_area, Area, Rect};

struct Triangle {
    base: f64,
    height: f64,
}

impl Area for Triangle {
    fn area(&self) -> f64 {
        self.base * self.height / 2.0
    }
}

struct Unit;

impl Area for Unit {
    fn area(&self) -> f64 {
        1.0
    }
}

#[test]
fn a_type_the_crate_never_saw() {
    assert_eq!(total_area(&[Triangle { base: 4.0, height: 3.0 }, Triangle { base: 2.0, height: 2.0 }]), 8.0);
}

#[test]
fn a_zero_sized_type() {
    assert_eq!(total_area(&[Unit, Unit, Unit]), 3.0);
}

#[test]
fn rect_area_directly() {
    assert_eq!(Rect { w: 0.5, h: 8.0 }.area(), 4.0);
}
