use std::io;
fn main() {
    println!("Please input your number.");
    let mut num = String::new();
    //println!("string::new = {guess}");

    //call the stdin function from the io module 
    io::stdin() //This line can be => std::io::stdin(:we won't need importing std::io in the beginning) 
        .read_line(&mut num)//take whatever the user types into standard input and append that into a string. & => refrence we need to make it mutable => &mut
        .expect("Failed to read line");//We’re still working on  line 8 of code
    // all 8-10 can be => io::stdin().read_line(&mut guess).expect("Failed to read line");
    let num: u32 = num.trim().parse().expect("Please type a number!");
    if num % 2 == 0 {
        println!("your number is even");
    }else {
        println!("your number is odd");
    }
    
}