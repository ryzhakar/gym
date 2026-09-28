use u01_probe_a_p3::{shift_all, Point};

#[test]
fn signature_is_unchanged() {
    let _: fn(&[Point], Point) -> Vec<Point> = shift_all;
}

#[test]
fn no_points() {
    assert!(shift_all(&[], Point { x: 5, y: 5 }).is_empty());
}

#[test]
fn three_points_negative_offset() {
    let points = [Point { x: 1, y: 1 }, Point { x: 0, y: 0 }, Point { x: -2, y: 4 }];
    let got = shift_all(&points, Point { x: -1, y: -2 });
    assert_eq!(got, vec![Point { x: 0, y: -1 }, Point { x: -1, y: -2 }, Point { x: -3, y: 2 }]);
}

#[test]
fn no_clone_call() {
    assert!(!include_str!("../src/lib.rs").contains(".clone()"), "src/lib.rs calls .clone()");
}
