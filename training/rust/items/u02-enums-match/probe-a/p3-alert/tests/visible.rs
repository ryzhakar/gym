use u02_probe_a_p3::{alert, Status};

#[test]
fn temperatures() {
    assert_eq!(alert(Status::Temp(45)), Some("heat 45".to_string()));
    assert_eq!(alert(Status::Temp(-25)), Some("frost -25".to_string()));
    assert_eq!(alert(Status::Temp(20)), None);
}

#[test]
fn humidity() {
    assert_eq!(alert(Status::Humidity(95)), Some("damp 95".to_string()));
    assert_eq!(alert(Status::Humidity(50)), None);
}

#[test]
fn battery() {
    assert_eq!(alert(Status::Battery { percent: 5, charging: false }), Some("battery 5".to_string()));
    assert_eq!(alert(Status::Battery { percent: 5, charging: true }), None);
    assert_eq!(alert(Status::Battery { percent: 80, charging: false }), None);
}

#[test]
fn missing() {
    assert_eq!(alert(Status::Missing), Some("no data".to_string()));
}
