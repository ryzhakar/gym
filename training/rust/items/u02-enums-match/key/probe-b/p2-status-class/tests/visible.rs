use u02_probe_b_p2::{class, Response};

#[test]
fn each_class_once() {
    assert_eq!(class(Response::Status(101)), "info");
    assert_eq!(class(Response::Status(204)), "success");
    assert_eq!(class(Response::Status(304)), "moved");
    assert_eq!(class(Response::Status(404)), "client error");
    assert_eq!(class(Response::Status(503)), "server error");
    assert_eq!(class(Response::Timeout), "retry");
    assert_eq!(class(Response::Redirect(String::from("/home"))), "follow");
}
