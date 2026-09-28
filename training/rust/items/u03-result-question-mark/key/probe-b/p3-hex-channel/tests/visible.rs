use u03_probe_b_p3::{brightest, ChannelError};

#[test]
fn largest_channel() {
    assert_eq!(brightest(&["0a", "ff", "7c"]), Ok(255));
}

#[test]
fn no_channels() {
    assert_eq!(brightest(&[]), Err(ChannelError::Empty));
}

#[test]
fn bad_channel_in_the_middle() {
    assert_eq!(brightest(&["10", "zz", "ff"]), Err(ChannelError::BadChannel { index: 1 }));
}
