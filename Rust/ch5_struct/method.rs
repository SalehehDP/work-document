#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}
//Defining Methods
impl Rectangle {
    fn area(&self) -> u32 {
        self.width * self.height
    }

    fn can_hold(&self , another : &Rectangle) -> bool{
        return (self.width > another.width && self.height > another.height)
    }
    //associated function
    fn square(size : u32) -> Rectangle{
        Rectangle {
            width : size,
            height : size,
        }
    }
}
fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };
    let rect2 = Rectangle{
        width : 10,
        height : 40,
    };
    let rect3 = Rectangle{
        width : 20,
        height : 80,
    };

    println!(
        "The area of the rectangle is {} square pixels.",
        rect1.area()
    );
    println!("Can rect1 hold rect2? {}", rect1.can_hold(&rect2));
    println!("Can rect1 hold rect3? {}", rect1.can_hold(&rect3));
    
    // associated function
    let sq = Rectangle::square(3);
    println!("square is : {:#?}" , sq);
}