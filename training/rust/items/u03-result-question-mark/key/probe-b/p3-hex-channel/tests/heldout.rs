use u03_probe_b_p3::{brightest, ChannelError};

const SOURCE: &str = include_str!("../src/lib.rs");

fn code() -> String {
    SOURCE
        .lines()
        .map(|line| match line.find("//") {
            Some(at) => &line[..at],
            None => line,
        })
        .collect::<Vec<_>>()
        .join("\n")
}

#[test]
fn no_panic_on_input() {
    let code = code();
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!code.contains(banned), "src/lib.rs uses `{banned}`");
    }
}

#[test]
fn signature_is_kept() {
    let _: fn(&[&str]) -> Result<u8, ChannelError> = brightest;
}

#[test]
fn enum_is_kept() {
    fn variants(e: ChannelError) -> usize {
        match e {
            ChannelError::Empty => 0,
            ChannelError::BadChannel { index } => index,
        }
    }
    assert_eq!(variants(ChannelError::BadChannel { index: 7usize }), 7);
}

#[test]
fn bad_channel_first() {
    assert_eq!(brightest(&["g0", "ff"]), Err(ChannelError::BadChannel { index: 0 }));
}

#[test]
fn bad_channel_last() {
    assert_eq!(brightest(&["01", "02", "100"]), Err(ChannelError::BadChannel { index: 2 }));
}

#[test]
fn bad_channel_alone() {
    assert_eq!(brightest(&["xyz"]), Err(ChannelError::BadChannel { index: 0 }));
    assert_eq!(brightest(&[""]), Err(ChannelError::BadChannel { index: 0 }));
}

#[test]
fn first_of_two_bad_channels() {
    assert_eq!(brightest(&["ff", "q", "r"]), Err(ChannelError::BadChannel { index: 1 }));
}

#[test]
fn single_good_channel() {
    assert_eq!(brightest(&["00"]), Ok(0));
    assert_eq!(brightest(&["FF"]), Ok(255));
}
