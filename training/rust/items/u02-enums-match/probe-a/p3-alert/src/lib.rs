pub enum Status {
    Temp(i32),
    Humidity(u8),
    Battery { percent: u8, charging: bool },
    Missing,
}

/// The alert text for `s`, or `None` when there is nothing to report.
pub fn alert(s: Status) -> Option<String> {
    todo!()
}
