//! Readings as one struct with fields. A test rejects this file if the keyword for sum types appears in it, comments included.

pub struct Reading {
    temperature: Option<i32>,
    fault: Option<u8>,
}


pub fn temp(celsius: i32) -> Reading { Reading{temperature: Some(celsius), fault: None} }
pub fn fault(code: u8) -> Reading { Reading{fault: Some(code), temperature: None} }
pub fn off() -> Reading { Reading{temperature: None, fault: None} }
pub fn fault_code(r: Reading) -> Option<u8> {
    r.fault
}
pub fn label(r: Reading) -> String {
    let label = match r {
        Reading{temperature: Some(degrees), ..} => {
            if degrees < 0 { format!("freezing {degrees}") }
            else if degrees >= 30 { format!("hot {degrees}") }
            else { format!("temp {degrees}") }
        }
        Reading{fault: Some(code), ..} => {
            if code == 0 { format!("fault unknown") }
            else { format!("fault {code}") }
        }
        Reading{..} => format!("off")
    };
    label.to_owned()
}
