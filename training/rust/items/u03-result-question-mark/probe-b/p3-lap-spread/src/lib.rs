#[derive(Debug, PartialEq)]
pub enum LapError {
    Empty,
    BadLap { position: usize },
}

#[derive(Debug, PartialEq)]
pub struct Spread {
    pub fastest: u32,
    pub slowest: u32,
}

/// The fastest and slowest of the laps, written like "71;69;75".
pub fn spread(laps: &str) -> Result<Spread, LapError> {
    let mut fields = Vec::new();
    for field in laps.split_terminator(';') {
        fields.push(field);
    }
    let mut fastest: u32 = fields[0].parse().unwrap();
    let mut slowest = fastest;
    for field in fields {
        let lap: u32 = field.parse().unwrap();
        if lap < fastest {
            fastest = lap;
        }
        if lap > slowest {
            slowest = lap;
        }
    }
    Ok(Spread { fastest, slowest })
}
