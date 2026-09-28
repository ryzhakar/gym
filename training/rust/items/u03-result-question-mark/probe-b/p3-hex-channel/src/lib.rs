#[derive(Debug, PartialEq)]
pub enum ChannelError {
    Empty,
    BadChannel { index: usize },
}

/// The largest of the channel values, each written in hexadecimal.
pub fn brightest(channels: &[&str]) -> Result<u8, ChannelError> {
    let mut best = u8::from_str_radix(channels[0], 16).unwrap();
    for channel in channels {
        let value = u8::from_str_radix(channel, 16).unwrap();
        if value > best {
            best = value;
        }
    }
    Ok(best)
}
