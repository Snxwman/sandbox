use std::collections::HashMap;

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut seen: HashMap<i32, i32> = HashMap::new();

        for (i, num) in nums.iter().enumerate() {
            let remainder = target - num;

            if let Some(&j) = seen.get(&remainder) {
                return vec![j, i as i32];
            }

            seen.insert(*num as i32, i as i32);
        }

        unreachable!()
    }
}
