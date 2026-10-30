/// One `name: value` header line, borrowed from the text it was parsed from.
pub struct Header<'a> {
    pub name: &'a str,
    pub value: &'a str,
}

impl<'a> Header<'a> {
    pub fn parse(line: &'a str) -> Option<Header<'a>> {
        let (name, value) = line.split_once(": ")?;
        Some(Header { name, value })
    }

    /// Borrows the line, not the header: the result outlives `self`.
    pub fn main_value(&self) -> &'a str {
        match self.value.split_once(';') {
            Some((main, _)) => main,
            None => self.value,
        }
    }
}
