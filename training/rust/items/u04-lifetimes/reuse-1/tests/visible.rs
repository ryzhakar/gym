use std::path::Path;
use std::process::Command;

const CASES: u32 = 6;

/// `ok`, or the code of the first error rustc reports for the case.
fn verdict(case: u32) -> String {
    let root = Path::new(env!("CARGO_MANIFEST_DIR"));
    let out = std::env::temp_dir().join(format!("u04-reuse-1-{}", std::process::id()));
    let output = Command::new("rustc")
        .args(["--edition", "2021", "--crate-type", "lib", "--emit=metadata"])
        .args(["--crate-name", &format!("case{case}")])
        .arg("--out-dir")
        .arg(&out)
        .arg(root.join("cases").join(format!("{case}.rs")))
        .output()
        .expect("rustc runs");
    let stderr = String::from_utf8_lossy(&output.stderr);
    match stderr.find("error[E") {
        Some(at) => stderr[at + 6..at + 11].to_string(),
        None if output.status.success() => "ok".to_string(),
        None => "no code".to_string(),
    }
}

#[test]
fn prediction_matches_rustc() {
    let text = std::fs::read_to_string(Path::new(env!("CARGO_MANIFEST_DIR")).join("prediction.txt"))
        .expect("prediction.txt is readable");
    let lines: Vec<&str> = text.lines().map(str::trim).filter(|l| !l.is_empty()).collect();
    assert!(lines.len() == CASES as usize, "prediction.txt needs one line per case, {CASES} in all");
    let mut wrong = 0;
    for case in 1..=CASES {
        let predicted = lines
            .iter()
            .find_map(|l| l.split_once(' ').filter(|(n, _)| n.trim() == case.to_string()))
            .map(|(_, v)| v.trim().to_string());
        if predicted.as_deref() != Some(verdict(case).as_str()) {
            wrong += 1;
        }
    }
    assert!(wrong == 0, "prediction.txt does not match rustc");
}
