enum Token {
    Num(i64),
    Op(char),
    Word(String),
    End,
}

fn show(t: Token) -> String {
    match t {
        Token::Num(n) if n < 0 => format!("negative {n}"),
        Token::Num(0) => "zero".to_string(),
        Token::Num(n @ 1..=9) => format!("digit {n}"),
        Token::Num(n) => format!("number {n}"),
        Token::Op('+' | '-') => "additive".to_string(),
        Token::Op(c) => format!("operator {c}"),
        Token::Word(w) if w.len() > 3 => format!("long {w}"),
        Token::Word(w) => format!("word {w}"),
        Token::End => "end".to_string(),
    }
}

fn main() {
    let tokens = vec![
        Token::Num(-4),
        Token::Num(0),
        Token::Num(9),
        Token::Num(10),
        Token::Op('-'),
        Token::Op('*'),
        Token::Word("abcd".to_string()),
        Token::Word("abc".to_string()),
        Token::End,
    ];
    for t in tokens {
        println!("{}", show(t));
    }
}
