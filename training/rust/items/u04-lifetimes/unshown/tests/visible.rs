use u04_unshown::{after, swap};

#[test]
fn after_the_marker() {
    assert_eq!(after("to: ada", ": "), "ada");
    assert_eq!(after("a=b=c", "="), "b=c");
}

#[test]
fn after_without_the_marker() {
    assert_eq!(after("plain", "="), "plain");
}

#[test]
fn swap_the_sides() {
    assert_eq!(swap("key=value", "="), "value=key");
    assert_eq!(swap("a=b=c", "="), "b=c=a");
}

#[test]
fn swap_without_the_marker() {
    assert_eq!(swap("plain", "="), "plain");
}

#[test]
fn results_outlive_the_marker() {
    let line = String::from("name -> ada");
    let rest;
    let swapped;
    {
        let marker = String::from(" -> ");
        rest = after(&line, &marker);
        swapped = swap(&line, &marker);
    }
    assert_eq!(rest, "ada");
    assert_eq!(swapped, "ada -> name");
}
