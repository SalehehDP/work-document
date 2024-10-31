fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}
fn main(){
    let mut s = String::from("hello"); //from is a function that conver &str to String 
    // The book : This kind of string can be mutated but literals cannot 
    //The book : we know the contents at compile time
    
    //trying 
    let mut st: &str = "hello";
    st = "hello!!!";
    print_type_of(&st);
    let st_2 : String = "!!!".to_owned() + st; // + can't be done in compile time ? 
    print_type_of(&"  ".to_owned());
    print_type_of(&st_2);
    //?? 


    s.push_str(", world!"); // push_str() appends a literal to a String
    println!("{}", s); 
    
    //Move : 
    let s1 = String::from("hello");
    let s2 = s1;
    //println!("{}, world!", s1);  // Error :  borrow of moved value: `s1`
    let s3 = String::from("hello");
    // s3 comes into scope
    takes_ownership(s3);// s3's value moves into the function...
                        // ... and so is no longer valid here
    
    //Clone :
    let s1 = String::from("hello");
    let s2 = s1.clone();
    println!("s1 = {}, s2 = {}", s1, s2);
}
fn takes_ownership(some_string: String) { // some_string comes into scope
    println!("{}", some_string);
} // Here, some_string goes out of scope and `drop` is called. The backing  memory is freed.