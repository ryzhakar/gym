use u01_reuse_1::lift_below_top;

#[test]
fn lifts_everything_below_the_top() {
    let mut scores = vec![3, 9, 5, 9];
    assert_eq!(lift_below_top(&mut scores, 2), 9);
    assert_eq!(scores, vec![5, 9, 7, 9]);
}

#[test]
fn no_scores() {
    let mut scores: Vec<u32> = Vec::new();
    assert_eq!(lift_below_top(&mut scores, 5), 0);
    assert!(scores.is_empty());
}
