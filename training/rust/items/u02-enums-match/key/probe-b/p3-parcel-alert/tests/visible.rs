use u02_probe_b_p3::{alert, Parcel};

fn some(text: &str) -> Option<String> {
    Some(String::from(text))
}

#[test]
fn freight() {
    assert_eq!(alert(Parcel::Weighed { grams: 25000, fragile: false }), some("freight"));
}

#[test]
fn heavy() {
    assert_eq!(alert(Parcel::Weighed { grams: 7000, fragile: false }), some("heavy"));
}

#[test]
fn light_and_fragile() {
    assert_eq!(alert(Parcel::Weighed { grams: 300, fragile: true }), some("fragile"));
}

#[test]
fn light_and_sturdy() {
    assert_eq!(alert(Parcel::Weighed { grams: 300, fragile: false }), None);
}

#[test]
fn delayed_long() {
    assert_eq!(alert(Parcel::Delayed(4)), some("late 4 days"));
}

#[test]
fn delayed_short() {
    assert_eq!(alert(Parcel::Delayed(1)), None);
}

#[test]
fn lost() {
    assert_eq!(alert(Parcel::Lost), some("lost"));
}

#[test]
fn delivered() {
    assert_eq!(alert(Parcel::Delivered), None);
}
