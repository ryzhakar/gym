#[derive(Debug, PartialEq)]
pub struct Point {
    pub x: i32,
    pub y: i32,
}

/// Every point moved by `offset`, in order.
pub fn shift_all(points: &[Point], offset: Point) -> Vec<Point> {
    let mut out = Vec::new();
    for p in points {
        out.push(add(p, &offset));
    }
    out
}

fn add(a: &Point, b: &Point) -> Point {
    Point { x: a.x + b.x, y: a.y + b.y }
}
