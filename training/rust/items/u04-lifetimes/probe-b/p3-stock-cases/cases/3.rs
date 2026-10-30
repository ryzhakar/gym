pub fn clear_shelf(stock: &mut Vec<u32>) -> bool {
    let last = stock.last();
    stock.clear();
    last.is_some()
}
