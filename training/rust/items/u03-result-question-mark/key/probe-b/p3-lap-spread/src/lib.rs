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
    if laps.is_empty() {
        return Err(LapError::Empty);
    }
    let mut fastest = u32::MAX;
    let mut slowest = 0;
    let mut position = 0;
    for field in laps.split_terminator(';') {
        let lap: u32 = field.parse().map_err(|_| LapError::BadLap { position })?;
        if lap < fastest {
            fastest = lap;
        }
        if lap > slowest {
            slowest = lap;
        }
        position += 1;
    }
    Ok(Spread { fastest, slowest })
}
