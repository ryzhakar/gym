pub fn total(prices: &mut Vec<u32>, extra: u32) -> u32 {
    let first = &prices[0];
    let sum = first + extra;
    prices.push(extra);
    sum
}
