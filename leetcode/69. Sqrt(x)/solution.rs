impl Solution {
    pub fn my_sqrt(x: i32) -> i32 {
        let x = x as u64;
        let mut upperbound= x;
        let mut lowerbound= 0;

        while lowerbound <= upperbound {
            let midpoint = lowerbound + (upperbound - lowerbound) / 2;
            let guess = midpoint * midpoint;

            match guess {
                _ if guess > x => upperbound = midpoint - 1,
                _ if guess < x => {
                    if (midpoint+1) * (midpoint+1) > x {
                        return midpoint as i32;
                    }

                    lowerbound = midpoint + 1
                },
                _ => return midpoint as i32,
            }

        }
        unreachable!()
    }
}
