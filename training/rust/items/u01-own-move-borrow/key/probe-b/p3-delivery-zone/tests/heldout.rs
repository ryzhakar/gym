use u01_probe_b_p3::{count_covered, Zone};

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

// Compiles only while `Zone` is not `Clone`.
trait CloneProbe<Marker> {
    fn probe() {}
}

impl<T> CloneProbe<()> for T {}

struct WhenClone;

impl<T: Clone> CloneProbe<WhenClone> for T {}

#[test]
fn zone_is_not_clone() {
    <Zone as CloneProbe<_>>::probe();
}

#[test]
fn signature_is_kept() {
    let _: fn(Zone, &[u32]) -> usize = count_covered;
}

#[test]
fn zone_fields_are_kept() {
    let Zone { name, postcodes } = Zone { name: String::new(), postcodes: Vec::<u32>::new() };
    let _: (String, Vec<u32>) = (name, postcodes);
}

#[test]
fn no_orders() {
    let zone = Zone { name: String::from("east"), postcodes: vec![5] };
    assert_eq!(count_covered(zone, &[]), 0);
}

#[test]
fn one_order() {
    let zone = Zone { name: String::from("east"), postcodes: vec![5] };
    assert_eq!(count_covered(zone, &[5]), 1);
    let zone = Zone { name: String::from("east"), postcodes: vec![5] };
    assert_eq!(count_covered(zone, &[6]), 0);
}

#[test]
fn several_orders() {
    let zone = Zone { name: String::from("wide"), postcodes: vec![0, u32::MAX, 42] };
    assert_eq!(count_covered(zone, &[0, 1, u32::MAX, 42, 41, 42]), 4);
    let empty = Zone { name: String::new(), postcodes: Vec::new() };
    assert_eq!(count_covered(empty, &[0, 1, 2]), 0);
}

#[test]
fn no_clone_call() {
    let code: String = code().split_whitespace().collect();
    assert!(!code.contains("clone("), "src/lib.rs calls clone");
}
