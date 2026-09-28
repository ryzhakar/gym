macro_rules! form_tests {
    ($form:ident) => {
        mod $form {
            use u02_attempt::$form::{fault, fault_code, label, off, temp};

            #[test]
            fn hot_from_30() {
                assert_eq!(label(temp(30)), "hot 30");
                assert_eq!(label(temp(41)), "hot 41");
            }

            #[test]
            fn freezing_below_0() {
                assert_eq!(label(temp(-1)), "freezing -1");
            }

            #[test]
            fn plain_temp() {
                assert_eq!(label(temp(0)), "temp 0");
                assert_eq!(label(temp(29)), "temp 29");
            }

            #[test]
            fn faults() {
                assert_eq!(label(fault(0)), "fault unknown");
                assert_eq!(label(fault(7)), "fault 7");
            }

            #[test]
            fn off_label() {
                assert_eq!(label(off()), "off");
            }

            #[test]
            fn fault_codes() {
                assert_eq!(fault_code(fault(0)), Some(0));
                assert_eq!(fault_code(fault(9)), Some(9));
                assert_eq!(fault_code(temp(9)), None);
                assert_eq!(fault_code(off()), None);
            }
        }
    };
}

form_tests!(enum_form);
form_tests!(flat_form);

#[test]
fn enum_form_is_an_enum() {
    let src = include_str!("../src/enum_form.rs");
    assert!(src.contains("enum ") && src.contains("match "), "enum_form.rs needs an enum and a match");
}

#[test]
fn flat_form_has_no_enum() {
    assert!(!include_str!("../src/flat_form.rs").contains("enum"), "flat_form.rs contains `enum`");
}
