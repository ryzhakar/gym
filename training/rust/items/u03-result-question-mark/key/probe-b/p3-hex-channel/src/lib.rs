#[derive(Debug, PartialEq)]
pub enum ChannelError {
    Empty,
    BadChannel { index: usize },
}

/// The largest of the channel values, each written in hexadecimal.
pub fn brightest(channels: &[&str]) -> Result<u8, ChannelError> {
    if channels.is_empty() {
        return Err(ChannelError::Empty);
    }
    let mut best = 0;
    let mut index = 0;
    for channel in channels {
        let value = u8::from_str_radix(channel, 16).map_err(|_| ChannelError::BadChannel { index })?;
        if value > best {
            best = value;
        }
        index += 1;
    }
    Ok(best)
}
