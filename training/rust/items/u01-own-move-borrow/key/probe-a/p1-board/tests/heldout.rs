use u01_probe_a_p1::Board;

#[test]
fn signature_is_unchanged() {
    let _: fn(&mut Board, u32) -> u32 = Board::record;
}

#[test]
fn empty_board() {
    let mut board = Board { scores: Vec::new() };
    assert_eq!(board.record(3), 0);
    assert_eq!(board.record(1), 3);
    assert_eq!(board.scores, vec![3, 1]);
}

#[test]
fn vector_not_copied() {
    let src = include_str!("../src/lib.rs");
    assert!(!src.contains("clone()") && !src.contains("to_vec"), "the vector is copied");
}
