pub enum Status {
    Temp(i32),
    Humidity(u8),
    Battery { percent: u8, charging: bool },
    Missing,
}

/// The alert text for `s`, or `None` when there is nothing to report.
pub fn alert(s: Status) -> Option<String> {
    match s {
        Status::Temp(t @ 40..) => Some(format!("heat {t}")),
        Status::Temp(t @ ..=-20) => Some(format!("frost {t}")),
        Status::Temp(..) => None,
        Status::Humidity(h @ 91..) => Some(format!("damp {h}")),
        Status::Humidity(..) => None,
        Status::Battery { charging: true, .. } => None,
        Status::Battery { percent: p @ 0..=9, .. } => Some(format!("battery {p}")),
        Status::Battery { .. } => None,
        Status::Missing => Some("no data".to_string()),
    }
}
