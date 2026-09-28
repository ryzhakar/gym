use u03_reuse_2::{withdraw, TxError};

#[test]
fn zero_balance() {
    assert_eq!(withdraw(0, "1"), Err(TxError::Insufficient { balance: 0, amount: 1 }));
    assert_eq!(withdraw(0, "0"), Err(TxError::Zero));
}

#[test]
fn negative_is_bad_amount() {
    assert!(matches!(withdraw(5, "-1"), Err(TxError::BadAmount(_))));
}

#[test]
fn largest_amount() {
    assert_eq!(withdraw(u64::MAX, "18446744073709551615"), Ok(0));
    assert!(matches!(withdraw(u64::MAX, "18446744073709551616"), Err(TxError::BadAmount(_))));
}

#[test]
fn subtraction_decides_and_nothing_panics() {
    let src = include_str!("../src/lib.rs");
    assert!(src.contains("checked_sub"), "no checked_sub in src/lib.rs");
    assert!(src.contains('?'), "no `?` in src/lib.rs");
    for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
        assert!(!src.contains(banned), "src/lib.rs contains `{banned}`");
    }
}
