//! Readings as one struct with fields. A test rejects this file if the keyword for sum types appears in it, comments included.
//! Define `Reading` here, then the five functions below.

const TEMP: u8 = 0;
const FAULT: u8 = 1;
const OFF: u8 = 2;

/// `kind` says which field means something: `celsius` for TEMP, `code` for FAULT, neither for OFF.
pub struct Reading {
    kind: u8,
    celsius: i32,
    code: u8,
}

pub fn temp(celsius: i32) -> Reading {
    Reading { kind: TEMP, celsius, code: 0 }
}

pub fn fault(code: u8) -> Reading {
    Reading { kind: FAULT, celsius: 0, code }
}

pub fn off() -> Reading {
    Reading { kind: OFF, celsius: 0, code: 0 }
}

pub fn label(r: Reading) -> String {
    if r.kind == TEMP {
        if r.celsius >= 30 {
            format!("hot {}", r.celsius)
        } else if r.celsius < 0 {
            format!("freezing {}", r.celsius)
        } else {
            format!("temp {}", r.celsius)
        }
    } else if r.kind == FAULT {
        if r.code == 0 {
            "fault unknown".to_string()
        } else {
            format!("fault {}", r.code)
        }
    } else {
        "off".to_string()
    }
}

pub fn fault_code(r: Reading) -> Option<u8> {
    if r.kind == FAULT {
        Some(r.code)
    } else {
        None
    }
}
