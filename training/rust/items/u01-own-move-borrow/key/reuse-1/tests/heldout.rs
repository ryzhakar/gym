use u01_reuse_1::lift_below_top;

#[test]
fn signature_is_unchanged() {
    let _: fn(&mut Vec<u32>, u32) -> u32 = lift_below_top;
}

#[test]
fn all_equal_nothing_lifted() {
    let mut scores = vec![4, 4, 4];
    assert_eq!(lift_below_top(&mut scores, 10), 4);
    assert_eq!(scores, vec![4, 4, 4]);
}

#[test]
fn lifted_past_the_old_top_still_returns_the_old_top() {
    let mut scores = vec![1, 2];
    assert_eq!(lift_below_top(&mut scores, 5), 2);
    assert_eq!(scores, vec![6, 2]);
}

#[test]
fn works_on_the_vector_in_place() {
    let mut scores = vec![1, 7, 3];
    let buffer = scores.as_ptr();
    lift_below_top(&mut scores, 1);
    assert_eq!(scores.as_ptr(), buffer);
    let src = include_str!("../src/lib.rs");
    assert!(!src.contains("clone()") && !src.contains("to_vec"), "the vector is copied");
}
