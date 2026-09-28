pub enum Parcel {
    Weighed { grams: u32, fragile: bool },
    Delayed(u32),
    Lost,
    Delivered,
}

/// The alert for a parcel, if it needs one.
pub fn alert(parcel: Parcel) -> Option<String> {
    todo!()
}
