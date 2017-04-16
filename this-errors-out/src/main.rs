use std::io::Read;
use std::fs::File;

fn main() {
    let mut file = File::open("/etc/service.conf").unwrap();
    let mut contents = String::new();
    file.read_to_string(&mut contents).unwrap();
    println!("{}", &contents);
}
