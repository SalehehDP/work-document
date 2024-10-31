fn main(){
    //Looping Through a Collection : for 
    
    let a = [10, 20, 30, 40, 50];
    for element in a {
        println!("the value is: {element}");
    }


    //countdown 
    for number in (1..4).rev() {
        println!("{number}!");
    }
    println!("LIFTOFF!!!");

    //do rondom thing with for : 
    let num : i32 = 100;
    let mut sum : i32 = 0;
    for i in 1..num+1 {
        sum += i;
    }
    println!("the sum of num from 1 to 100 = {}" , sum);
    //break
    for i in 1..100{
        println!("break work in 'for'!");
        if i == 1{
            break; 
        }
    }

    //range : 
    //what is the end
    let mut final_num = 0; // Is it possible to define a variable without giving an initial value ?? 
    for i in 1..101{
         final_num = i;
    }
    println!("in range 1..101 the final number is : {final_num}");
    final_num = 0;
    for i in 1..=100{
        final_num = i;
    }
    println!("in range 1..=100 the final number is : {final_num}");


    


    
}
