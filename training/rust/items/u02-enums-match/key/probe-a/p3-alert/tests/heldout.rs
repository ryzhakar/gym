use u02_probe_a_p3::{alert, Status};

#[test]
fn boundaries() {
    assert_eq!(alert(Status::Temp(40)), Some("heat 40".to_string()));
    assert_eq!(alert(Status::Temp(39)), None);
    assert_eq!(alert(Status::Temp(-20)), Some("frost -20".to_string()));
    assert_eq!(alert(Status::Temp(-19)), None);
    assert_eq!(alert(Status::Humidity(91)), Some("damp 91".to_string()));
    assert_eq!(alert(Status::Humidity(90)), None);
    assert_eq!(alert(Status::Battery { percent: 9, charging: false }), Some("battery 9".to_string()));
    assert_eq!(alert(Status::Battery { percent: 10, charging: false }), None);
    assert_eq!(alert(Status::Battery { percent: 0, charging: true }), None);
}

#[test]
fn every_arm_names_its_variant() {
    let src = include_str!("../src/lib.rs");
    assert!(!src.contains("_ =>") && !src.contains("_=>"), "src/lib.rs has a `_` arm");
}
