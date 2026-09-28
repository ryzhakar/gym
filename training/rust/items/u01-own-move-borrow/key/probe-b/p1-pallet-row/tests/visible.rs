use u01_probe_b_p1::{push_front, Pallet};

fn pallet(label: &str, weight_kg: u32) -> Pallet {
    Pallet { label: String::from(label), weight_kg }
}

#[test]
fn returns_the_old_front_weight() {
    let mut row = vec![pallet("A1", 40), pallet("B7", 25)];
    assert_eq!(push_front(&mut row, pallet("C3", 90)), Some(40));
    assert_eq!(row.len(), 3);
    assert_eq!(row[0].label, "C3");
    assert_eq!(row[1].label, "A1");
    assert_eq!(row[2].label, "B7");
}
