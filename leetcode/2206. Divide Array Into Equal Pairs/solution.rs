use std::collections::HashSet;

impl Solution {
    pub fn divide_array(nums: Vec<i32>) -> bool {
        let mut set = HashSet::new();
        for num in nums {
            if set.contains(&num) {
                set.remove(&num);
            } else {
                set.insert(num);
            }
        }

        set.len() == 0
    }
}
