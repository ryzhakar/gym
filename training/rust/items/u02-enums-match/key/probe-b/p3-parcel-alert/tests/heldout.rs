use u02_probe_b_p3::{alert, Parcel};

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

fn some(text: &str) -> Option<String> {
    Some(String::from(text))
}

fn weighed(grams: u32, fragile: bool) -> Option<String> {
    alert(Parcel::Weighed { grams, fragile })
}

#[test]
fn signature_is_kept() {
    let _: fn(Parcel) -> Option<String> = alert;
}

#[test]
fn enum_is_kept() {
    fn variants(p: Parcel) -> u8 {
        match p {
            Parcel::Weighed { grams: _, fragile: _ } => 0,
            Parcel::Delayed(_) => 1,
            Parcel::Lost => 2,
            Parcel::Delivered => 3,
        }
    }
    assert_eq!(variants(Parcel::Weighed { grams: 1u32, fragile: true }), 0);
    assert_eq!(variants(Parcel::Delayed(1u32)), 1);
}

#[test]
fn weight_boundaries_sturdy() {
    assert_eq!(weighed(0, false), None);
    assert_eq!(weighed(4999, false), None);
    assert_eq!(weighed(5000, false), some("heavy"));
    assert_eq!(weighed(19999, false), some("heavy"));
    assert_eq!(weighed(20000, false), some("freight"));
    assert_eq!(weighed(u32::MAX, false), some("freight"));
}

#[test]
fn weight_boundaries_fragile() {
    assert_eq!(weighed(0, true), some("fragile"));
    assert_eq!(weighed(4999, true), some("fragile"));
    assert_eq!(weighed(5000, true), some("heavy"));
    assert_eq!(weighed(19999, true), some("heavy"));
    assert_eq!(weighed(20000, true), some("freight"));
}

#[test]
fn delay_boundaries() {
    assert_eq!(alert(Parcel::Delayed(0)), None);
    assert_eq!(alert(Parcel::Delayed(2)), None);
    assert_eq!(alert(Parcel::Delayed(3)), some("late 3 days"));
    assert_eq!(alert(Parcel::Delayed(u32::MAX)), some("late 4294967295 days"));
}

#[test]
fn no_wildcard_arm() {
    let code = code();
    for (at, _) in code.match_indices("=>") {
        let mut back = code[..at].trim_end().chars().rev();
        let wildcard = back.next() == Some('_')
            && !back.next().map_or(false, |c| c.is_alphanumeric() || c == '_');
        assert!(!wildcard, "src/lib.rs has a `_` arm");
    }
    assert!(!code.contains(" _ if "), "src/lib.rs has a `_` arm");
}
