fn main(){

    let s = String::from("hello");
    let slice_st = &s[0..2];
    let slice_st = &s[..2]; // start value default is 0     

    let len = s.len();
    let slice_end = &s[3..len];
    let slice_end = &s[3..];// end value will be length by default 
    // entire string => 
    let slice_ent = &s[0..len];
    let slice_ent = &s[..];


}