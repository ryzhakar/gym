fn main() {
    let mut seen = 0;
    let doubled = [3, 8, 5, 12].iter().map(|&x| {
        println!("map {x}");
        x * 2
    });
    println!("built");
    let big: Vec<i32> = doubled
        .filter(|&y| {
            seen += 1;
            println!("filter {y}");
            y > 10
        })
        .take(1)
        .collect();
    println!("{big:?} {seen}");
}
