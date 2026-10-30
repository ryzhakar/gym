//! A reader over the `key=value` pieces of a query. See spec.md.

pub struct Pairs<'a> {
    rest: &'a str,
}

impl<'a> Pairs<'a> {
    pub fn new(query: &'a str) -> Pairs<'a> {
        Pairs { rest: query }
    }

    pub fn next_pair(&mut self) -> Option<(&'a str, &'a str)> {
        while !self.rest.is_empty() {
            let piece = match self.rest.split_once(';') {
                Some((piece, tail)) => {
                    self.rest = tail;
                    piece
                }
                None => {
                    let piece = self.rest;
                    self.rest = "";
                    piece
                }
            };
            if !piece.is_empty() {
                return Some(piece.split_once('=').unwrap_or((piece, "")));
            }
        }
        None
    }
}
