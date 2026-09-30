pub struct Queue {
    pub tracks: Vec<String>,
}

impl Queue {
    /// Moves the front track to the back. Returns the byte length of the new front track,
    /// or 0 when the queue is empty.
    fn cycle(&mut self) -> usize {
        if self.tracks.is_empty() {
            return 0;
        }
        let front = self.tracks.remove(0);
        self.tracks.push(front);
        self.tracks[0].len()
    }
}

/// Calls `cycle` once per requested cycle and records what each call returned, in order.
pub fn cycle_count_history(mut queue: Queue, times: u32) -> Vec<usize> {
    let mut history = Vec::new();
    for _ in 0..times {
        history.push(queue.cycle());
    }
    history
}
