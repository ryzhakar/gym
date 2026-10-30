use u04_reuse_4::{entries, first_message, Entry};

#[test]
fn a_message_may_hold_colons() {
    let entry = Entry::parse("INFO api: retry: 3 of 5").unwrap();
    assert_eq!(entry.source(), "api");
    assert_eq!(entry.message(), "retry: 3 of 5");
}

#[test]
fn the_first_match_wins() {
    let log = "WARN a: one\nWARN b: two";
    assert_eq!(first_message(log, "WARN").unwrap(), "one");
}

#[test]
fn an_empty_log() {
    assert!(entries("").is_empty());
    assert!(first_message("", "INFO").is_none());
}

#[test]
fn level_and_source_outlive_their_entry() {
    let line = String::from("DEBUG cache: miss");
    let (level, source) = {
        let entry = Entry::parse(&line).unwrap();
        (entry.level(), entry.source())
    };
    assert_eq!(level, "DEBUG");
    assert_eq!(source, "cache");
}

#[test]
fn a_message_outlives_the_list_of_entries() {
    let log = String::from("INFO api: started\nERROR db: down");
    let message = {
        let all = entries(&log);
        all[1].message()
    };
    assert_eq!(message, "down");
}

#[test]
fn a_temporary_level_and_a_missing_one() {
    let log = String::from("INFO api: started");
    let found = first_message(&log, &String::from("INFO"));
    let missing = first_message(&log, &String::from("WARN"));
    assert_eq!(found.unwrap(), "started");
    assert!(missing.is_none());
}
