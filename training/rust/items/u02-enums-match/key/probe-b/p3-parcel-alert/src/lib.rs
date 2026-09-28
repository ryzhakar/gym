pub enum Parcel {
    Weighed { grams: u32, fragile: bool },
    Delayed(u32),
    Lost,
    Delivered,
}

/// The alert for a parcel, if it needs one.
pub fn alert(parcel: Parcel) -> Option<String> {
    match parcel {
        Parcel::Weighed { grams: 20000.., .. } => Some(String::from("freight")),
        Parcel::Weighed { grams: 5000..=19999, .. } => Some(String::from("heavy")),
        Parcel::Weighed { fragile: true, .. } => Some(String::from("fragile")),
        Parcel::Weighed { fragile: false, .. } => None,
        Parcel::Delayed(days @ 3..) => Some(format!("late {days} days")),
        Parcel::Delayed(_) => None,
        Parcel::Lost => Some(String::from("lost")),
        Parcel::Delivered => None,
    }
}
