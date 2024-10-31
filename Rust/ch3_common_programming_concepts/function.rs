fn main() {
    let tup_1 = (1 , 2 , 's' , 23.3); // ! tuple can't have string !
    let arr :[u8 ; 5] = [1 ; 5];
    print_everything(5, 'h' , tup_1 , arr); // call a func with parameters
}

fn print_everything( x : i32 , ch : char , tup_1 : (i32 , i32 , char , f32) , arr : [u8;5]){

    let (int_1 , int_2 , ch_2 , float_1) = tup_1;
    let first_ind = arr[0];
    
    println!("i32 : {x} , char : {ch} , tuple : ({int_1} , {int_2} , {ch_2} , {float_1}) , array first index : {first_ind}");
}
