/// Adds `count` to `stock` and returns the largest count held before the addition.
pub fn restock(stock: &mut Vec<u32>, count: u32) -> Option<u32> {
    let before = stock.iter().max();
    stock.push(count);
    before.copied()
}
