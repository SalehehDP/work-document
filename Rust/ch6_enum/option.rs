#[derive(Debug)]
enum Option<T> {
    Some(T),
    None
}

fn main() {
    let greeting = Some("Hello, World");
    println!("{:?}", greeting);
    
    let some_number = Some(5);
    let some_string = Some("a string");
    
    let absent_number: Option<i32> = None; // we are getting error!! mismatched types
}

