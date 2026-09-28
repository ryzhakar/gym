use u01_probe_a_p1::Board;

#[test]
fn returns_the_best_before_the_new_score() {
    let mut board = Board { scores: vec![4, 11, 7] };
    assert_eq!(board.record(20), 11);
    assert_eq!(board.scores, vec![4, 11, 7, 20]);
}
