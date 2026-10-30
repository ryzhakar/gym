//! A reader over the comma-separated fields of one line. See spec.md.

pub struct Row<'a> {
    rest: Option<&'a str>,
}

impl<'a> Row<'a> {
    pub fn new(line: &'a str) -> Row<'a> {
        Row { rest: Some(line) }
    }

    pub fn next_field(&mut self) -> Option<&'a str> {
        let rest = self.rest?;
        match rest.split_once(',') {
            Some((field, tail)) => {
                self.rest = Some(tail);
                Some(field)
            }
            None => {
                self.rest = None;
                Some(rest)
            }
        }
    }
}
