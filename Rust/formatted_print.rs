fn main(){    
    let name = "Saleheh";
    let st = format!("my firstname is : {name}"); // write formatted text to String
    print!("{st} and my lastname is : {last}" , last = "Davarpanah"); //same as format! but the text is printed to the console (io::stdout).
    print!("\n"); // same as print! but a newline is appended.


    //println!
    let x = 5;
    let y = 10;
    println!("x = {} and y = {}", x, y);
    println!("x = {x} and y = {y}");
    // Positional arguments can be used. Specifying an integer inside `{}`
    // determines which additional argument will be replaced. Arguments start
    // at 0 immediately after the format string
    println!("x = {0} and y = {1}" , x , y);
    // As can named arguments.
    println!("x = {first} and y = {second}" , first = 5 , second = 10);
    //or another example for naming argument :
    println!("{subject} {verb} {object}",
             object="the lazy dog",
             subject="the quick brown fox",
             verb="jumps over"); 

    // Different formatting can invoked by specified format character after a ':'
    println!("Base 10 repr:               {}",   69420);
    println!("Base 2 (binary) repr:       {:b}", 69420);
    println!("Base 8 (octal) repr:        {:o}", 69420);
    println!("Base 16 (hexadecimal) repr: {:x}", 69420);

    // You can right-align text with a specified width. This will output "     1". 5 white spaces and a "1".
    println!("{number:>5}", number=1);
    // You can pad numbers with extra zeroes. This will output "000001".
    println!("{number:0>5}", number=1);
    // You can use named arguments in the format specifier by appending a `$`
    println!("{number:0>width$}", number=1, width=5);
    //
    let number = 1;
    let width  = 6;
    println!("{number:>width$}");

    let arr = [21 ; 10];
    //println!("first index = {arr[0]}"); *error*
    println!("first index = {}" , arr[0]);
    let width1 = 30;
    let height1 = 50;
    println!(
        "The area of the rectangle is {} square pixels.",
        area(width1, height1));
}
fn area(width: u32, height: u32) -> u32 {
    width * height
}