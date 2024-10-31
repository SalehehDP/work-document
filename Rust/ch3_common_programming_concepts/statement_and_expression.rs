fn main() {

    let x = 6; //statment : does not return value 

    /*

    let x = (let y = 6);   &&    let x = let y = 6;
    error: expected expression, found statement (`let`)
    = note: variable declaration using `let` is a statement

    let x = y = 6;
    error : cannot find value `y` in this scope

    */

    // 6 , 5 + 6  , Calling a function , Calling a macro , { }  , if =>  expressions
    //Expressions can be part of statements:
    let y = {
        let z = 3;
        z + 1  // => Expressions do not include ending semicolons. If you add a semicolon to the end of an expression, you turn it into a statement
    };  // this block evaluates to 4
    println!("The value of y is: {y}");

    //Using if in a let Statement
    let condition = true;
    let number = if condition { 5 } else { 6 };


}