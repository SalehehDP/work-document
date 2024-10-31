fn main(){

    // Conditional Loops : while 
    let mut number = 3;
    while number != 0 {
        println!("{number}!");
        number -= 1;
    }
    println!("LIFTOFF!!!");

    //loop over the elements of a collection
    let a = [10, 20, 30, 40, 50];
    let mut index = 0;
    while index < 5 { //we could cause the program to panic if the index value or test condition are incorrect
        println!("the value is: {}", a[index]);
        index += 1; 
    }

    // return value with while ?? 
    let mut counter = 0;
    let x = while counter < 10{
        counter += 1;
    } // does't work maybe with break => make it to be loop ? 
    println!("counter : {}" , counter);


}