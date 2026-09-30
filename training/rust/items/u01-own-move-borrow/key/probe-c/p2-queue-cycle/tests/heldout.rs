use u01_probe_c_p2::{cycle_count_history, Queue};

fn queue(tracks: &[&str]) -> Queue {
    Queue { tracks: tracks.iter().map(|t| t.to_string()).collect() }
}

#[test]
fn signature_is_unchanged() {
    let _: fn(Queue, u32) -> Vec<usize> = cycle_count_history;
}

#[test]
fn empty_queue() {
    assert_eq!(cycle_count_history(queue(&[]), 4), vec![0, 0, 0, 0]);
}

#[test]
fn zero_cycles() {
    assert!(cycle_count_history(queue(&["a", "bb"]), 0).is_empty());
}

#[test]
fn one_track_never_changes() {
    assert_eq!(cycle_count_history(queue(&["solo"]), 3), vec![4, 4, 4]);
}

#[test]
fn full_lap_returns_to_the_start() {
    let lengths = cycle_count_history(queue(&["ab", "cde", "f"]), 6);
    assert_eq!(lengths, vec![3, 1, 2, 3, 1, 2]);
}

#[test]
fn no_copies() {
    let src = include_str!("../src/lib.rs");
    for banned in ["clone", "to_owned", "to_vec", "to_string"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}
