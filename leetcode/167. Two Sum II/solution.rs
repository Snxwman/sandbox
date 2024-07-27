impl Solution {
    pub fn two_sum(numbers: Vec<i32>, target: i32) -> Vec<i32> {
        let mut lp = 0;
        let mut rp = numbers.len()-1;

        while lp < rp {
            let sum = numbers[lp] + numbers[rp];

            match sum {
                _ if sum == target => return vec![(lp + 1) as i32, (rp + 1) as i32],
                _ if sum < target => lp += 1,
                _ if sum > target => rp -= 1,
                _ => unreachable!()
            }
        }

        unreachable!()
    }
}
