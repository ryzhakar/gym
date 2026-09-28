use u01_probe_b_p1::{push_front, Pallet};

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

fn pallet(label: &str, weight_kg: u32) -> Pallet {
    Pallet { label: String::from(label), weight_kg }
}

#[test]
fn signature_is_kept() {
    let _: fn(&mut Vec<Pallet>, Pallet) -> Option<u32> = push_front;
}

#[test]
fn pallet_is_kept() {
    let Pallet { label, weight_kg } = Pallet { label: String::new(), weight_kg: 0u32 };
    let _: (String, u32) = (label, weight_kg);
}

#[test]
fn empty_row_gives_none() {
    let mut row = Vec::new();
    assert_eq!(push_front(&mut row, pallet("Z9", 5)), None);
    assert_eq!(row.len(), 1);
    assert_eq!(row[0].weight_kg, 5);
}

#[test]
fn weight_is_the_one_from_before_the_insert() {
    let mut row = vec![pallet("A1", 0)];
    assert_eq!(push_front(&mut row, pallet("B2", u32::MAX)), Some(0));
    assert_eq!(push_front(&mut row, pallet("C3", 7)), Some(u32::MAX));
    assert_eq!(push_front(&mut row, pallet("D4", 7)), Some(7));
    assert_eq!(row.len(), 4);
    assert_eq!(row[3].label, "A1");
}

#[test]
fn surviving_pallets_keep_their_strings() {
    let mut row = vec![pallet("A1", 40), pallet("B7", 25)];
    let before: Vec<*const u8> = row.iter().map(|p| p.label.as_ptr()).collect();
    let incoming = pallet("C3", 90);
    let incoming_at = incoming.label.as_ptr();
    push_front(&mut row, incoming);
    assert_eq!(row[0].label.as_ptr(), incoming_at);
    assert_eq!(row[1].label.as_ptr(), before[0]);
    assert_eq!(row[2].label.as_ptr(), before[1]);
}

#[test]
fn no_clone() {
    assert!(!code().contains("clone"), "src/lib.rs uses clone");
}
