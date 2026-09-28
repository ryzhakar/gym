use u01_probe_b_p1::restock;

#[test]
fn returns_the_maximum_from_before_the_addition() {
    let mut stock = vec![3, 9, 4];
    assert_eq!(restock(&mut stock, 12), Some(9));
    assert_eq!(stock, vec![3, 9, 4, 12]);
}
