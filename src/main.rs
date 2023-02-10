use serde_json;
use std::env;
use std::fs::metadata;
use std::fs::File;
use walkdir::WalkDir;

fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() != 2 {
        println!("Invalid number of arguments. Usage: `yeetdir [path]");
        std::process::exit(0);
    }

    run(&args[1]);
}

fn run(target_path: &str) {
    match metadata(target_path) {
        Ok(m) if m.is_dir() => pack(target_path),
        Ok(m) if m.is_file() => {
            if !target_path.ends_with(".json") {
                println!("invalid file");
            }
            unpack(target_path);
        }
        _ => println!("Invalid path"),
    }
}

fn pack(target_path: &str) {
    let j = serde_json::to_string(
        r#"{ "kid":"kid-value",
    "kty":"RSA",
    "use":"sig",
    "n":"n-value",
    "e":"e-value" }"#,
    )
    .unwrap();

    println!("{}", j);

    for path in WalkDir::new(target_path)
        .into_iter()
        .filter_map(Result::ok)
        .filter(|e| e.file_type().is_file())
    {
        println!("{:?}", path);
    }
}

fn unpack(target_path: &str) {
    let mut file = File::open(target_path);
}
