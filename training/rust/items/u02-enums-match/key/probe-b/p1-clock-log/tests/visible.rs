use std::process::Command;

fn normalize(text: &str) -> String {
    text.lines()
        .map(str::trim_end)
        .collect::<Vec<_>>()
        .join("\n")
        .trim_end()
        .to_string()
}

#[test]
fn prediction_matches_the_output() {
    let output = Command::new(env!("CARGO_BIN_EXE_u02-probe-b-p1"))
        .output()
        .expect("the program runs");
    let actual = String::from_utf8(output.stdout).expect("the output is UTF-8");
    let predicted = std::fs::read_to_string(concat!(env!("CARGO_MANIFEST_DIR"), "/prediction.txt"))
        .expect("prediction.txt is readable");
    assert!(
        normalize(&actual) == normalize(&predicted),
        "prediction.txt does not match the program's output"
    );
}
