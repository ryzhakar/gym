pub struct Zone {
    pub name: String,
    pub postcodes: Vec<u32>,
}

impl Zone {
    pub fn covers(&self, postcode: u32) -> bool {
        for &p in self.postcodes.iter() {
            if p == postcode {
                return true;
            }
        }
        false
    }
}

/// Counts the orders whose postcode lies in `zone`.
pub fn count_covered(zone: Zone, orders: &[u32]) -> usize {
    let mut n = 0;
    for &postcode in orders {
        if zone.covers(postcode) {
            n += 1;
        }
    }
    n
}
