fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}
struct Color(i32, i32, i32);
struct Point(i32, i32, i32);

//unit struct
struct AlwaysEqual;
fn main() {
    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);
    print_type_of(&black); //output => tuple_struct::Color

    let subject = AlwaysEqual;
    print_type_of(&subject); //output => tuple_struct::AlwaysEqual
}