use u04_probe_b_p1::{bracketed, domain_or};

#[test]
fn bracketed_outlives_the_markers() {
    let header = String::from("Ann <ann@mail.org>");
    let inside: &str;
    {
        let open = String::from("<");
        let close = String::from(">");
        inside = bracketed(&header, &open, &close);
    }
    assert_eq!(inside, "ann@mail.org");
}

#[test]
fn bracketed_without_markers() {
    let whole: &str = bracketed("ann@mail.org", "<", ">");
    assert_eq!(whole, "ann@mail.org");
    assert_eq!(bracketed("Ann <ann@mail.org", "<", ">"), "ann@mail.org");
}

#[test]
fn domain_or_takes_the_part_after_the_at() {
    let domain: &str = domain_or("ann@mail.org", "local");
    assert_eq!(domain, "mail.org");
}

#[test]
fn domain_or_falls_back() {
    assert_eq!(domain_or("ann", "local"), "local");
}
