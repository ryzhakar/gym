use u01_probe_b_p1::restock;

const SOURCE: &str = include_str!("../src/lib.rs");

fn code() -> String {
    SOURCE
        .lines()
        .map(|line| match line.find("//") {
            Some(at) => &line[..at],
            None => line,
        })
        .collect::<Vec<_>>()
        .join("\n")
}

#[test]
fn signature_is_kept() {
    let _: fn(&mut Vec<u32>, u32) -> Option<u32> = restock;
}

#[test]
fn empty_stock_gives_none() {
    let mut stock = Vec::new();
    assert_eq!(restock(&mut stock, 5), None);
    assert_eq!(stock, vec![5]);
}

#[test]
fn smaller_count_keeps_the_old_maximum() {
    let mut stock = vec![7, 2];
    assert_eq!(restock(&mut stock, 1), Some(7));
    assert_eq!(stock, vec![7, 2, 1]);
}

#[test]
fn repeated_restocks_each_report_the_maximum_before_them() {
    let mut stock = Vec::new();
    assert_eq!(restock(&mut stock, 4), None);
    assert_eq!(restock(&mut stock, 10), Some(4));
    assert_eq!(restock(&mut stock, 10), Some(10));
    assert_eq!(restock(&mut stock, 1), Some(10));
    assert_eq!(stock, vec![4, 10, 10, 1]);
}

#[test]
fn stock_is_not_copied() {
    let code = code();
    for banned in ["clone", "to_vec", "to_owned", "collect"] {
        assert!(!code.contains(banned), "src/lib.rs uses `{banned}`");
    }
}
