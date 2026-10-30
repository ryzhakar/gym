/// The stop after `from` on `route`, whose stops are separated by spaces, as in `"Ash Birch Cedar"`.
/// `from` itself when it is the last stop or not on the route.
pub fn next_stop<'a>(route: &'a str, from: &'a str) -> &'a str {
    let mut stops = route.split_whitespace();
    while let Some(stop) = stops.next() {
        if stop == from {
            return stops.next().unwrap_or(from);
        }
    }
    from
}

/// The platform of `stop` on `board`, one `stop=platform` line per stop, as in `"Ash=2\nBirch=5"`.
/// `fallback` when `stop` has no line.
pub fn platform<'a>(board: &'a str, stop: &str, fallback: &'a str) -> &'a str {
    for line in board.lines() {
        if let Some((name, number)) = line.split_once('=') {
            if name == stop {
                return number;
            }
        }
    }
    fallback
}
