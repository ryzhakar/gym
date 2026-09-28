use u03_reuse_2::{withdraw, TxError};

#[test]
fn takes_the_amount() {
    assert_eq!(withdraw(100, "30"), Ok(70));
    assert_eq!(withdraw(100, "100"), Ok(0));
}

#[test]
fn bad_amount() {
    assert!(matches!(withdraw(100, "ten"), Err(TxError::BadAmount(_))));
}

#[test]
fn zero() {
    assert_eq!(withdraw(100, "0"), Err(TxError::Zero));
}

#[test]
fn insufficient() {
    assert_eq!(withdraw(20, "50"), Err(TxError::Insufficient { balance: 20, amount: 50 }));
}
