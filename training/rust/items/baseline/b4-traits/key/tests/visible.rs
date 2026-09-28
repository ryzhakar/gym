use b4_traits::{total_area, Area, Rect, Square};

#[test]
fn rects() {
    assert_eq!(total_area(&[Rect { w: 2.0, h: 3.0 }, Rect { w: 1.0, h: 4.0 }]), 10.0);
}

#[test]
fn squares() {
    assert_eq!(total_area(&[Square(3.0)]), 9.0);
    assert_eq!(Square(2.0).area(), 4.0);
}

#[test]
fn empty() {
    let none: [Rect; 0] = [];
    assert_eq!(total_area(&none), 0.0);
}
