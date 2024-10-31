fn main() {

    // if 
    let number = 6;
    /*if condition {  //condition in this code must be a bool unlike python (and Ruby and JavaScript)
        --------      
    } else {
        --------
    }*/
    if number < 5 {
        println!("condition was true");
    } else {
        println!("condition was false");
    }

    //else if => Handling Multiple Conditions
    if number % 4 == 0 {
        println!("number is divisible by 4");
    } else if number % 3 == 0 {
        println!("number is divisible by 3");
    } else if number % 2 == 0 {
        println!("number is divisible by 2");
    } else {
        println!("number is not divisible by 4, 3, or 2");
    }

    /* // error : `if` and `else` have incompatible types
    let number = if condition { 5 }else { 6 };
    //or 
    let number = if condition { 5 } else { "six" };
    */
    
}