use u01_probe_b_p3::{count_inside, Band};

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
    let _: fn(Band, &[i32]) -> usize = count_inside;
}

#[test]
fn fields_are_kept() {
    let band = Band { low: -5i32, high: 5i32 };
    let Band { low, high } = band;
    assert_eq!((low, high), (-5, 5));
}

#[test]
fn no_readings() {
    assert_eq!(count_inside(Band { low: 0, high: 10 }, &[]), 0);
}

#[test]
fn one_reading_inside_and_one_outside() {
    assert_eq!(count_inside(Band { low: -3, high: -1 }, &[-2]), 1);
    assert_eq!(count_inside(Band { low: -3, high: -1 }, &[0]), 0);
}

#[test]
fn several_readings_at_and_beyond_the_bounds() {
    let band = Band { low: -10, high: -10 };
    assert_eq!(count_inside(band, &[-11, -10, -9, -10, i32::MIN, i32::MAX]), 2);
    let wide = Band { low: i32::MIN, high: i32::MAX };
    assert_eq!(count_inside(wide, &[i32::MIN, 0, i32::MAX]), 3);
}

#[test]
fn no_clone_call() {
    let code: String = code().split_whitespace().collect();
    assert!(!code.contains("clone("), "src/lib.rs calls clone");
}
