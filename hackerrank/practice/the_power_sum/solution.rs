use std::io;

macro_rules! read_n {
    ( $name : ident, $typ : ty ) => {
        let mut line : String = String::new();
        io::stdin().read_line(&mut line);
        let $name : $typ = line.trim().parse::<$typ>().expect("invalid data type");
    };
}


fn main() {
    read_n!(x, u32);
    read_n!(n, u32);

    let mut powers : Vec<u32> = (1..32).map(|x: u32| x.pow(n)).collect();
    let mut no_of_ways: u32 = 0;

    permut(x, 0, &mut powers, 0, &mut no_of_ways);

    println!("{}", no_of_ways);
}


fn permut(x: u32, sum: u32, mut powers: &mut Vec<u32>, start: usize, mut no_of_ways: &mut u32)  {
    if sum == x {
        *no_of_ways += 1;
        return;
    }

    if powers.len() == 0 || sum > x {
        return;
    }

    for i in start..powers.len() {
        permut(x, sum + powers[i], &mut powers, i + 1, &mut no_of_ways);
    }
}

