fn main() {

    // loop : forever or until you explicitly tell it to stop.( in terminal : ctrl + C )
    // break : program when to stop executing the loop.
    // continue : in a loop tells the program to skip over any remaining code in this iteration of the loop and go to the next iteration.
    let mut i = 0;
    loop {
        i += 1;
        if i > 10 {
            break;
        }
        if i == 5{
            continue;
        }
        println!("The i is {i}");
    }

    //Returning Values from Loops
    let mut counter = 0;
    let result = loop {
        counter += 1;
        if counter == 10 {
            break counter * 2;
        }
    };
    println!("The result is {result}"); // result = 20 

    //Loop Labels
    let mut count = 0;
    'counting_up: loop {
        println!("count = {count}");
        let mut remaining = 10;
        loop {
            println!("remaining = {remaining}");
            if remaining == 9 {
                break;
            }
            if count == 2 {
                break 'counting_up; // with loop labels we can use break or continue to specify that those keywords apply to the labeled loop instead of the innermost loop
            }   
            remaining -= 1;
        }
        count += 1;
    }
    println!("End count = {count}");
}