fn func_1() -> i32 {
    6 // or return 6
}

fn plus_one(x: i32) -> i32 {
    x + 1
}

fn main() {
    let y = func_1();
    let x = plus_one(y);
    println!("The value of x is: {x}");

    let tup = func_with_two_ret();
    let (x , y) = tup;
    println!("function with two return : ({x} , {y})");

}


fn func_with_two_ret() -> (i32 , f32){
    (32 , 32.)
}