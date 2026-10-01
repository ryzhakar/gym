//! Readings as an enum. Define `Reading` here as an enum, then the five functions below.


pub enum Reading {
    Temperature(i32),
    Fault(u8),
    Off,
}


pub fn temp(celsius: i32) -> Reading { Reading::Temperature(celsius) }
pub fn fault(code: u8) -> Reading { Reading::Fault(code) }
pub fn off() -> Reading { Reading::Off }
pub fn fault_code(r: Reading) -> Option<u8> {
    match r {
        Reading::Fault(code) => {Some(code)}
        _ => { None }
    }
}
pub fn label(r: Reading) -> String {
    let label = match r {
        Reading::Temperature(degrees) => {
            if degrees < 0 { format!("freezing {degrees}") }
            else if degrees >= 30 { format!("hot {degrees}") }
            else { format!("temp {degrees}") }
        }
        Reading::Fault(code) => {
            if code == 0 { format!("fault unknown") }
            else { format!("fault {code}") }
        }
        Reading::Off => format!("off")
    };
    label.to_owned()
}
