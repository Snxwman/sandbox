impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        use std::collections::HashSet;
        let hashset: HashSet<i32> = HashSet::from_iter(nums.iter().cloned());
        hashset.len() != nums.len()
    }
}
