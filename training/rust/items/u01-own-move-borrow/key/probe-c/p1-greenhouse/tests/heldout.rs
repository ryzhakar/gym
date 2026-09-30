use u01_probe_c_p1::{grow_short_plants, Plant};

fn bed(pairs: &[(&str, u32)]) -> Vec<Plant> {
    pairs.iter().map(|&(name, height_cm)| Plant { name: name.into(), height_cm }).collect()
}

#[test]
fn signature_is_unchanged() {
    let _: fn(&mut Vec<Plant>, u32) -> u32 = grow_short_plants;
}

#[test]
fn all_equal_nothing_grown() {
    let mut b = bed(&[("a", 5), ("b", 5)]);
    assert_eq!(grow_short_plants(&mut b, 9), 5);
    assert_eq!(b.iter().map(|p| p.height_cm).collect::<Vec<_>>(), vec![5, 5]);
}

#[test]
fn grown_past_the_old_top_still_returns_the_old_top() {
    let mut b = bed(&[("a", 1), ("b", 2)]);
    assert_eq!(grow_short_plants(&mut b, 5), 2);
    assert_eq!(b.iter().map(|p| p.height_cm).collect::<Vec<_>>(), vec![6, 2]);
}

#[test]
fn works_on_the_vector_in_place() {
    let mut b = bed(&[("a", 1), ("b", 7), ("c", 3)]);
    let buffer = b.as_ptr();
    grow_short_plants(&mut b, 1);
    assert_eq!(b.as_ptr(), buffer);
}

#[test]
fn no_copies() {
    let src = include_str!("../src/lib.rs");
    for banned in ["clone", "to_owned", "to_vec", "to_string"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}
