fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}
fn main(){
    {// s is not valid here, it’s not yet declared
        let s = "hello";// s is valid from this point forward
        print_type_of(&s);// do stuff with s
    }   // this scope is now over, and s is no longer valid


    let x = 2;
    {
        println!("{x}");
    }

}