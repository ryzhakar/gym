pub struct Plant {
    pub name: String,
    pub height_cm: u32,
}

fn tallest(bed: &[Plant]) -> &Plant {
    bed.iter().max_by_key(|p| p.height_cm).expect("bed is not empty")
}

/// Adds `growth` to every plant shorter than the tallest plant.
/// Returns the tallest plant's height from before the change.
pub fn grow_short_plants(bed: &mut Vec<Plant>, growth: u32) -> u32 {
    let top_height = tallest(bed).height_cm;
    for p in bed.iter_mut() {
        if p.height_cm < top_height {
            p.height_cm += growth;
        }
    }
    top_height
}
