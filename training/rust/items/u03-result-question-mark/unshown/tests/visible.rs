use u03_unshown::{parse_reading, ReadError};

#[test]
fn reads_a_number() {
    assert_eq!(parse_reading(b" 42\n"), Ok(42));
}

#[test]
fn not_utf8() {
    assert!(matches!(parse_reading(&[0xff, 0x31]), Err(ReadError::Utf8(_))));
}

#[test]
fn not_a_number() {
    assert!(matches!(parse_reading(b"4 2"), Err(ReadError::Number(_))));
}

#[test]
fn both_std_errors_convert_into_read_error() {
    let number_error = "x".parse::<u32>().unwrap_err();
    assert_eq!(ReadError::from(number_error.clone()), ReadError::Number(number_error));
    let bytes = vec![0xc3, 0x28];
    let utf8_error = std::str::from_utf8(&bytes).unwrap_err();
    assert_eq!(ReadError::from(utf8_error), ReadError::Utf8(utf8_error));
}
