use u04_probe_b_p1::{bracketed, domain_or};

#[test]
fn bracketed_outlives_markers_of_any_length() {
    let header = String::from("Subject: [ops] [urgent] disk full");
    let tag: &str;
    {
        let open = String::from("[");
        let close = String::from("] ");
        tag = bracketed(&header, &open, &close);
    }
    assert_eq!(tag, "ops");
}

#[test]
fn bracketed_takes_the_first_open_and_the_next_close() {
    assert_eq!(bracketed("a(b)c(d)", "(", ")"), "b");
    assert_eq!(bracketed(")x(y", "(", ")"), "y");
    assert_eq!(bracketed("<>", "<", ">"), "");
}

#[test]
fn domain_or_borrows_from_owned_inputs() {
    let address = String::from("bo@post.example");
    let default = String::from("localhost");
    let domain: &str = domain_or(&address, &default);
    assert_eq!(domain, "post.example");
    let plain = String::from("bo");
    let fallback: &str = domain_or(&plain, &default);
    assert_eq!(fallback, "localhost");
}

#[test]
fn domain_or_splits_at_the_first_at() {
    assert_eq!(domain_or("a@b@c", "x"), "b@c");
    assert_eq!(domain_or("a@", "x"), "");
}
