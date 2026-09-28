use u01_probe_b_p3::{count_covered, Zone};

fn north() -> Zone {
    Zone { name: String::from("north"), postcodes: vec![1010, 1020] }
}

#[test]
fn counts_covered_orders() {
    assert_eq!(count_covered(north(), &[1010, 3000, 1020, 1010]), 3);
}

#[test]
fn the_zone_is_still_there_after_the_loop() {
    let zone = north();
    let mut covered = 0;
    for postcode in [1010, 3000, 1020] {
        if zone.covers(postcode) {
            covered += 1;
        }
    }
    assert_eq!(covered, 2);
    assert_eq!(zone.name, "north");
}
