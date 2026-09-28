use std::num::ParseIntError;

#[derive(Debug, PartialEq)]
pub struct Point {
    pub x: i32,
    pub y: i32,
}

#[derive(Debug, PartialEq)]
pub enum PointError {
    /// No `,` in the input.
    MissingComma,
    /// The part before the first `,` is not an `i32`.
    BadX(ParseIntError),
    /// The part after the first `,` is not an `i32`.
    BadY(ParseIntError),
}

/// Parses `"x,y"`.
pub fn parse_point(text: &str) -> Result<Point, PointError> {
    let (x, y) = text.split_once(',').ok_or(PointError::MissingComma)?;
    let x = x.parse::<i32>().map_err(PointError::BadX)?;
    let y = y.parse::<i32>().map_err(PointError::BadY)?;
    Ok(Point { x, y })
}
