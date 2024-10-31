fn main() {

    //tuple 
    let tup :(i32 , f32 , i32) = (500, 6.4, 1); // wrong  let tup : tuple = (500, 6.4, 1);
    let (x , y , z) = tup;

    println!("tup = ({x} , {y} , {z})"); // destructuring

    let x = tup.0;
    let y = tup.1;
    let z = tup.2;
    let sum = tup.0 + tup.2;
    println!("tup = ({x} , {y} , {z}) , sum = {sum}"); //directly


    //array
    let a = [1, 2, 3, 4, 5];

    // name_array : [type of each element ; length of the array ] = [   ]
    let a: [i32; 5] = [1, 2, 3, 4, 5]; 

    //contain the same value
    let a = [3; 5]; // == a = [ 3 , 3 , 3 , 3 ,3 ];

    let first = a[0];
    let second = a[1];

}