//Deﬁning Structs 
#[derive(Debug)]
struct User { // struct name { fields   }
    active: bool, // name : type ,
    username: String,
    email: String,
    sign_in_count: u64,
}

fn main() {
    //Instantiating Structs 
    let mut user1 = User {
        email: String::from("someone@example.com"),
        username: String::from("someusername123"),
        active: true,
        sign_in_count: 1,
    };
    user1.email = String::from("anotheremail@example.com");

    //
    let user2 = build_user(String::from("haha@gmail.com") , String::from("haha"));

    //Struct Update Syntax : 
    //create a new instance of a struct that includes most of the values from another instance
    let user3 = User {
        active: user1.active,
        username: user1.username,
        email: String::from("another@example.com"),
        sign_in_count: user1.sign_in_count,
    };
    //println!("{}" , user1.username);//borrow of moved value: `user1.username`
    let user3 = User {
        email: String::from("another@example.com"),
        ..user2 //the remaining ﬁelds not explicitly set should have the same value as the ﬁelds in the given instance.
    };
    println!("{}" , user2.active); 
    
    //How print a struct : 
    //println!("the structure is : {}" , user3); // Error : `User` doesn't implement `std::fmt::Display` 
    println!("the structure is : {:?}" , user3); //without #[derive(Debug)] =>  Error : `User` doesn't implement `Debug` 
    println!("the structure is : {:#?}" , user3);
    dbg!(&user3);

    
}

fn build_user(email: String, username: String) -> User {
    User {
        //Field Init Shorthand
        email, //smae name  => email : email,
        username, // username : username ,
        active: true,
        sign_in_count: 2,
    }
}