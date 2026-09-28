use u03_attempt::LineError;

fn count_error(text: &str) -> LineError {
    match text.parse::<u32>() {
        Err(e) => LineError::BadCount(e),
        Ok(n) => panic!("test setup: {text} parsed as {n}"),
    }
}

macro_rules! form_tests {
    ($form:ident) => {
        mod $form {
            use super::count_error;
            use u03_attempt::$form::parse_line;
            use u03_attempt::LineError;

            #[test]
            fn good_line() {
                assert_eq!(parse_line("apples=12"), Ok(("apples", 12)));
            }

            #[test]
            fn splits_at_the_first_equals() {
                assert_eq!(parse_line("a=b=1"), Err(count_error("b=1")));
            }

            #[test]
            fn no_equals() {
                assert_eq!(parse_line("apples 12"), Err(LineError::NoEquals));
            }

            #[test]
            fn empty_name() {
                assert_eq!(parse_line("=12"), Err(LineError::EmptyName));
            }

            #[test]
            fn bad_count() {
                assert_eq!(parse_line("apples=-1"), Err(count_error("-1")));
                assert_eq!(parse_line("apples="), Err(count_error("")));
            }
        }
    };
}

form_tests!(explicit);
form_tests!(propagate);

#[test]
fn explicit_has_no_question_mark() {
    assert!(!include_str!("../src/explicit.rs").contains('?'), "explicit.rs contains `?`");
}

#[test]
fn propagate_uses_question_mark() {
    assert!(include_str!("../src/propagate.rs").contains('?'), "propagate.rs has no `?`");
}

#[test]
fn nothing_panics() {
    for src in [include_str!("../src/explicit.rs"), include_str!("../src/propagate.rs")] {
        for banned in ["unwrap", "expect", "panic!", "unreachable!", "todo!"] {
            assert!(!src.contains(banned), "src contains `{banned}`");
        }
    }
}
