pub fn shout(words: &mut Vec<String>) {
    let first = &words[0];
    words.push(String::from("hey"));
    println!("{first}");
}
