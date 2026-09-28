use u02_probe_b_p2::{class, Response};

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
fn signature_is_kept() {
    let _: fn(Response) -> &'static str = class;
}

#[test]
fn enum_is_kept() {
    fn variants(r: Response) -> u8 {
        match r {
            Response::Status(_) => 0,
            Response::Timeout => 1,
            Response::Redirect(_) => 2,
        }
    }
    assert_eq!(variants(Response::Status(0u16)), 0);
    assert_eq!(variants(Response::Redirect(String::new())), 2);
}

#[test]
fn every_boundary() {
    let cases = [
        (0, "info"),
        (199, "info"),
        (200, "success"),
        (299, "success"),
        (300, "moved"),
        (399, "moved"),
        (400, "client error"),
        (499, "client error"),
        (500, "server error"),
        (999, "server error"),
        (u16::MAX, "server error"),
    ];
    for (code, expected) in cases {
        assert_eq!(class(Response::Status(code)), expected, "status {code}");
    }
}

#[test]
fn empty_redirect_still_follows() {
    assert_eq!(class(Response::Redirect(String::new())), "follow");
}

#[test]
fn no_panicking_arm() {
    let code = code();
    for banned in ["panic!", "unreachable!", "todo!", "unimplemented!"] {
        assert!(!code.contains(banned), "src/lib.rs uses `{banned}`");
    }
}

#[test]
fn no_arm_added() {
    let arms = code().matches("=>").count();
    assert!(arms <= 7, "the match has {arms} arms, at most 7 allowed");
}
