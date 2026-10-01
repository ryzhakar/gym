pub enum Status {
    Temp(i32),
    Humidity(u8),
    Battery { percent: u8, charging: bool },
    Missing,
}

/// The alert text for `s`, or `None` when there is nothing to report.
pub fn alert(s: Status) -> Option<String> {
    match s {
        Status::Temp(t @ ..=-20) => Some(format!("frost {t}").to_string()),
        Status::Temp(t @ 40..) => Some(format!("heat {t}").to_string()),
        Status::Humidity(h @ 91..) => Some(format!("damp {h}").to_string()),
        Status::Missing => Some(format!("no data").to_string()),
        Status::Battery { charging: true, .. } => None,
        Status::Battery { percent: p @ ..10, charging: false } => Some(format!("battery {p}").to_string()),
        Status::Temp(_) | Status::Humidity(..) | Status::Battery { .. } => None,
    }
}
