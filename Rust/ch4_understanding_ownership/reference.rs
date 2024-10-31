fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}
fn main() {
    let s1 = String::from("hello");
    let len = calculate_length(&s1);
    println!("The length of '{}' is {}.", s1, len);
    
    //let s2 = String::from("hello");
    //change(&s2);
    //Mutable References : 
    let mut s2 = String::from("hello");
    change(&mut s2);
    //  *** cannot borrow `s` as mutable more than once at a time


    //what if i change a value after reference is declared ?
    let mut x = 100; 
    let refnc = &x;
    println!("{refnc}");
    //x = 234; // => Error : cannot assign to `x` because it is borrowed 
    println!("{refnc}");


}
/* 
fn change(some_string: &String) {
    some_string.push_str(", world"); //Eroor : reference are immutable by defult 
}
*/
fn change(some_string: &mut String) {
    some_string.push_str(", world");
}

fn calculate_length(s: &String) -> usize {
    print_type_of(&s);
    s.len()
}

/*Dangling References
fn dangle() -> &String {
    let s = String::from("hello");
    &s
} 
*/