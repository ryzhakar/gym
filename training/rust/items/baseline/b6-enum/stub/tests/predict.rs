use std::process::Command;

fn normalized(text: &str) -> String {
    let lines: Vec<&str> = text.lines().map(str::trim_end).collect();
    lines.join("\n").trim_end().to_string()
}

#[test]
fn prediction_matches_stdout() {
    // `cargo test` runs each test with the package root as its working directory.
    let predicted = std::fs::read_to_string("prediction.txt")
        .expect("prediction.txt is missing");
    assert!(!predicted.trim().is_empty(), "prediction.txt is empty");
    let run = Command::new(env!("CARGO_BIN_EXE_b6-enum")).output().expect("program did not start");
    let actual = String::from_utf8(run.stdout).expect("stdout is not UTF-8");
    // Never print the actual output: the learner predicts before seeing it.
    assert!(normalized(&predicted) == normalized(&actual), "prediction does not match stdout");
}
