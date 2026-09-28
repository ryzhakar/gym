use u01_probe_b_p3::{count_inside, Band};

#[test]
fn counts_readings_inside_the_band() {
    let band = Band { low: 18, high: 24 };
    assert_eq!(count_inside(band, &[17, 18, 21, 24, 25, 30]), 3);
}
