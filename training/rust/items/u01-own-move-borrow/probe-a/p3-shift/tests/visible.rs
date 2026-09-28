use u01_probe_a_p3::{shift_all, Point};

#[test]
fn shifts_every_point() {
    let points = [Point { x: 0, y: 0 }, Point { x: 2, y: -1 }];
    assert_eq!(shift_all(&points, Point { x: 1, y: 1 }), vec![Point { x: 1, y: 1 }, Point { x: 3, y: 0 }]);
}
