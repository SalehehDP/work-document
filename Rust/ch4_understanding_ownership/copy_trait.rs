fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}
fn main(){
    // copy values are stored in stack  => any group of simple scalar values can implement
    /*• All the integer types, such as u32 .
        • The Boolean type, bool , with values true and false .
        • All the ﬂoating point types, such as f64 .
        • The character type, char .
        • Tuples, if they only contain types that also implement Copy . For example, (i32, i32)
            implements Copy , but (i32, String) does not. */

    let x = 5;
    let y = x;
    println!("x = {}, y = {}", x, y);

    let z : u32 = x;
    println!("x = {}, z = {}", x, z);
    print_type_of(&x);


    let x = 5;
    makes_copy(x);// x would move into the function,
    // but i32 is Copy, so it's okay to still
    // use x afterward
}
fn makes_copy(some_integer: i32) { // some_integer comes into scope
    println!("{}", some_integer);
} // Here, some_integer goes out of scope. Nothing special happens.