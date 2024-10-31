#[derive(Debug)]
enum IpAddrKind {
    V4,
    V6,
}


fn print_ip( ip_kind : &IpAddrKind ){
    println!("{:#?}" , ip_kind);
    print_type_of(ip_kind);
    //println!("{:#?}" , IpKind);
}

enum LivingBeings{
    Plants(String),
    Animals(Animal),
}

enum Animal{
    Vertebrate(String),
    Invertebrates(String),
}



fn print_type_of<T>(_: &T) {
    println!("{}", std::any::type_name::<T>())
}

fn main(){
    //same type 
    let four = IpAddrKind::V4;
    let six = IpAddrKind::V6;

    print_ip(&four);
    print_ip(&six);

    let petos = LivingBeings::Plants(String::from("petos"));
    let me = LivingBeings::Animals(Animal::Vertebrate(String::from("human")));
    

}