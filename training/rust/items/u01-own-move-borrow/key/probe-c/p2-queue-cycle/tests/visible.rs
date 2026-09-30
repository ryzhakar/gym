use u01_probe_c_p2::{cycle_count_history, Queue};

fn queue(tracks: &[&str]) -> Queue {
    Queue { tracks: tracks.iter().map(|t| t.to_string()).collect() }
}

#[test]
fn cycles_three_times() {
    let q = queue(&["ab", "cde", "f"]);
    assert_eq!(cycle_count_history(q, 3), vec![3, 1, 2]);
}
