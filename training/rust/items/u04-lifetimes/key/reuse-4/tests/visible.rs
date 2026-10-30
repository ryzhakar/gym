use u04_reuse_4::{entries, first_message, Entry};

const LOG: &str = "INFO api: started\nWARN disk: 91% full\nnot a log line\nERROR db: connection lost\nWARN net: slow peer";

#[test]
fn parse_reads_the_three_parts() {
    let entry = Entry::parse("WARN disk: 91% full").unwrap();
    assert_eq!(entry.level(), "WARN");
    assert_eq!(entry.source(), "disk");
    assert_eq!(entry.message(), "91% full");
}

#[test]
fn parse_rejects_other_lines() {
    assert!(Entry::parse("WARN").is_none());
    assert!(Entry::parse("WARN disk 91% full").is_none());
}

#[test]
fn entries_skips_lines_that_do_not_parse() {
    let all = entries(LOG);
    assert_eq!(all.len(), 4);
    assert_eq!(all[2].source(), "db");
    assert_eq!(all[3].message(), "slow peer");
}

#[test]
fn first_message_at_a_level() {
    assert_eq!(first_message(LOG, "WARN").unwrap(), "91% full");
    assert_eq!(first_message(LOG, "ERROR").unwrap(), "connection lost");
    assert!(first_message(LOG, "DEBUG").is_none());
}

#[test]
fn a_message_outlives_its_entry() {
    let line = String::from("ERROR db: connection lost");
    let message = {
        let entry = Entry::parse(&line).unwrap();
        entry.message()
    };
    assert_eq!(message, "connection lost");
}

#[test]
fn the_level_asked_for_can_go_before_the_message_is_used() {
    let log = String::from(LOG);
    let message = {
        let level = String::from("ERROR");
        first_message(&log, &level)
    };
    assert_eq!(message.unwrap(), "connection lost");
}
