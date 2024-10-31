fn main() {

    let guess: u32 = "42".parse().expect("Not a number!");// need type <= parse()
    println!("{}" , guess);
        
    let num_hex = 0xff;
    let num_dec = 98_222;
    let num_oct = 0o77;
    let num_bin = 0b1111_0000;
    let num_btye = b'A'; // ASCII num
    println!("Hex:{num_hex}  Dec:{num_dec}  Oct:{num_oct}  Bin:{num_bin}  Byte:{num_btye}");

    //Integer Overﬂow
    let x: u8 = 255;
    //let x = x + 1;
    println!("{}" , x );

    //ﬂoating-point numbers
    let num_float = 2.0;
    let num_float_2: f32 = 3.00;
    println!("{} {} " , num_float , num_float_2);

    //Numeric Operations
    // addition
    let _sum = 5 + 10; // * names without _ : warning => if this is intentional, prefix it with an underscore: `_sum
    // subtraction
    let _difference = 95.5 - 4.3;
    // multiplication
    let _product = 4 * 30;
    // division
    let quotient = 56 / 32.2;
    let _floored = 2 / 3; // Results in 0
    // remainder
    let _remainder = 43 % 5;
    println!("quotient : {quotient}");

    //char
    //let ch : char = 1;
    let char_1 = 'z';
    let char_2: char = 'ℤ'; // with explicit type annotation
    let char_3 = '😀';
    println!("chars : {char_1} , {char_2} , {char_3}");
    println!("this is a string");
    
    let x : usize = 23;

}

