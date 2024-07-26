use std::collections::HashMap;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut freq: HashMap<i32, i32> = HashMap::new();

        for num in nums {
            freq.get_mut(&num)
                .and_then(|v| Some(*v += 1))
                .or_else(|| Some({freq.insert(num, 1);}));
        }

        let mut res: Vec<(i32, i32)> = freq.into_iter().collect();
        res.sort_by(|a, b| b.1.cmp(&a.1));

        res.into_iter()
            .map(|(n, _)| n)
            .take(k as usize)
            .collect()
    }
}

