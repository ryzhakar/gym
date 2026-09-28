pub enum Response {
    Status(u16),
    Timeout,
    Redirect(String),
}

/// Names the class of a response.
pub fn class(response: Response) -> &'static str {
    match response {
        Response::Timeout => "retry",
        Response::Redirect(_) => "follow",
        Response::Status(code) if code < 200 => "info",
        Response::Status(code) if code < 300 => "success",
        Response::Status(code) if code < 400 => "moved",
        Response::Status(code) if code < 500 => "client error",
        Response::Status(code) if code >= 500 => "server error",
    }
}
