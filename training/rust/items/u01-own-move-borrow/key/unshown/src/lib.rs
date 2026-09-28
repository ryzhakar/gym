pub struct Inbox {
    pub pending: Vec<String>,
    pub done: usize,
}

impl Inbox {
    /// Hands over every pending message, oldest first, and leaves none pending.
    /// `done` grows by the number handed over.
    pub fn drain_all(&mut self) -> Vec<String> {
        let all = std::mem::take(&mut self.pending);
        self.done += all.len();
        all
    }
}
