/// One line per recipient, in order: `"<recipient>: <msg>"`.
pub fn broadcast(recipients: &[String], msg: String) -> Vec<String> {
    let mut log = Vec::new();
    for r in recipients {
        log.push(deliver(r, msg));
    }
    log
}

fn deliver(to: &str, msg: String) -> String {
    format!("{to}: {msg}")
}
