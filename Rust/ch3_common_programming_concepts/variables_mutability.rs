fn main() {

    //let power
    let x = 6;
    let x = 7;
    println!("{}" , x);

    //immutable. => only read 
    /* Compiler error

    let x =6;
    x = 5;

    */

    // Mutable : you can't change the type 
    // & Constants 
    const NUM: i32 = 16;
    let y = 1;
    let mut ans = y * NUM;
    println!("{ans}");
    ans = NUM / y;
    println!("{}" ,ans);

    //Shadowing : change the value and type 
    let x = 5;
    let x = x + 1;
    {
        let x = x * 2;
        println!("The value of x in the inner scope is: {x}");
    }
    println!("The value of x is: {x}");

    //changing the type with shadowing
    let spaces = "       ";
    let spaces = spaces.len();
    println!("{}" , spaces);

    //let mut power 
    let mut spaces = "   ";
    let mut spaces = spaces.len();


    //mut
    let mut k = 0;
    k = k + 5;
    println!("{k}");

}