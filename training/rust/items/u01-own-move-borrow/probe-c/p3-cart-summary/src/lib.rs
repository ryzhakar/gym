pub struct Cart {
    pub items: Vec<String>,
}

impl Cart {
    /// Removes every item from the cart. Returns how many were removed.
    fn empty_out(mut self) -> usize {
        let n = self.items.len();
        self.items.clear();
        n
    }
}

/// `"<n> items cleared, now empty: <true/false>"`.
pub fn cart_summary(mut cart: Cart) -> String {
    let n = cart.empty_out();
    format!("{n} items cleared, now empty: {}", cart.items.is_empty())
}
