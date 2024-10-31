/*
why we need slices : 
    we have even more values that were
    calculated from data in a particular state but aren’t tied to that state at all. We have three unrelated
    variables ﬂoating around that need to be kept in sync.
*/
fn first_word(s: &String) -> usize { // we do't want ownership => & , return the last index first word => usize 
    let bytes = s.as_bytes(); // bytes is array of bytes in string 
    for (i, &item) in bytes.iter().enumerate() { // iter metod 
        if item == b' ' {
        return i;
        }   
    }
    s.len()
}

fn main(){
    let s = String::from("hello world");
    let hello = &s[0..5];
    let world = &s[6..11];

    let mut st = String::from("hello world");
    let word = first_word_with_slices(&st);
    //st.clear(); // error! => cannot borrow `st` as mutable because it is also borrowed as immutable
    println!("the first word is: {}", word);

    //Other Slices
    let a = [1, 2, 3, 4, 5];
    let slice = &a[1..3]; // => type &[i32]
    assert_eq!(slice, &[2, 3]);

}

fn first_word_with_slices(s: &String) -> &str {
    let bytes = s.as_bytes();
    for (i, &item) in bytes.iter().enumerate() {
        if item == b' ' {
        return &s[0..i];
        }
    }
    &s[..]
}