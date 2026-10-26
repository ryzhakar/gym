#[allow(dead_code)] // the fields are read only through Debug
#[derive(Debug)]
enum SeatError {
    NoDash,
    BadRow,
    BadSeat,
    NoSuchSeat { row: u32, seat: u32 },
}

fn seat_number(ticket: &str) -> Result<u32, SeatError> {
    let (row, seat) = ticket.split_once('-').ok_or(SeatError::NoDash)?;
    let seat = seat.parse::<u32>().map_err(|_| SeatError::BadSeat)?;
    let row = row.parse::<u32>().map_err(|_| SeatError::BadRow)?;
    if row > 20 || seat > 30 {
        return Err(SeatError::NoSuchSeat { row, seat });
    }
    Ok(row * 30 + seat)
}

fn main() {
    for ticket in ["3-12", "x-y", "7", "q-9", "25-31", "2-3-4"] {
        match seat_number(ticket) {
            Ok(number) => println!("{ticket}: seat {number}"),
            Err(error) => println!("{ticket}: {error:?}"),
        }
    }
}
