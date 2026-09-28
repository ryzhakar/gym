pub struct Pallet {
    pub label: String,
    pub weight_kg: u32,
}

/// Puts `incoming` at the front of the row and returns the weight of the pallet
/// that was at the front before.
pub fn push_front(row: &mut Vec<Pallet>, incoming: Pallet) -> Option<u32> {
    let front = row.first();
    let weight = match front {
        Some(pallet) => Some(pallet.weight_kg),
        None => None,
    };
    row.insert(0, incoming);
    weight
}
