pub struct Band {
    pub low: i32,
    pub high: i32,
}

fn contains(band: Band, reading: i32) -> bool {
    reading >= band.low && reading <= band.high
}

/// Counts the readings that lie inside `band`, bounds included.
pub fn count_inside(band: Band, readings: &[i32]) -> usize {
    let mut n = 0;
    for &reading in readings {
        if contains(band, reading) {
            n += 1;
        }
    }
    n
}
