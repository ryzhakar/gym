/// The part of `header` between the first `open` and the next `close` after it:
/// `"Ann <ann@mail.org>"` with `"<"` and `">"` gives `"ann@mail.org"`.
/// Everything after `open` when no `close` follows it; all of `header` when it holds no `open`.
pub fn bracketed<'a>(header: &'a str, open: &'a str, close: &'a str) -> &'a str {
    match header.split_once(open) {
        Some((_, rest)) => match rest.split_once(close) {
            Some((inside, _)) => inside,
            None => rest,
        },
        None => header,
    }
}

/// The part of `address` after its first `@`, or `default` when it has no `@`.
pub fn domain_or(address: &str, default: &str) -> &str {
    match address.split_once('@') {
        Some((_, domain)) => domain,
        None => default,
    }
}
