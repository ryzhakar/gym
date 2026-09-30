use u01_probe_c_p1::{grow_short_plants, Plant};

fn bed(pairs: &[(&str, u32)]) -> Vec<Plant> {
    pairs.iter().map(|&(name, height_cm)| Plant { name: name.into(), height_cm }).collect()
}

#[test]
fn grows_only_the_shorter_plants() {
    let mut b = bed(&[("fern", 4), ("oak", 11), ("moss", 7)]);
    assert_eq!(grow_short_plants(&mut b, 3), 11);
    assert_eq!(b.iter().map(|p| p.height_cm).collect::<Vec<_>>(), vec![7, 11, 10]);
}
