pub struct Board {
    pub scores: Vec<u32>,
}

impl Board {
    /// Appends `score`. Returns the best score from before the append, 0 when the board was empty.
    pub fn record(&mut self, score: u32) -> u32 {
        let best = *self.scores.iter().max().unwrap_or(&0);
        self.scores.push(score);
        best
    }
}
