//! Readings as an enum. Define `Reading` here as an enum, then the five functions below.

pub enum Reading {
    Temp(i32),
    Fault(u8),
    Off,
}

pub fn temp(celsius: i32) -> Reading {
    Reading::Temp(celsius)
}

pub fn fault(code: u8) -> Reading {
    Reading::Fault(code)
}

pub fn off() -> Reading {
    Reading::Off
}

pub fn label(r: Reading) -> String {
    match r {
        Reading::Temp(c) if c >= 30 => format!("hot {c}"),
        Reading::Temp(c) if c < 0 => format!("freezing {c}"),
        Reading::Temp(c) => format!("temp {c}"),
        Reading::Fault(0) => "fault unknown".to_string(),
        Reading::Fault(code) => format!("fault {code}"),
        Reading::Off => "off".to_string(),
    }
}

pub fn fault_code(r: Reading) -> Option<u8> {
    match r {
        Reading::Fault(code) => Some(code),
        Reading::Temp(_) | Reading::Off => None,
    }
}
