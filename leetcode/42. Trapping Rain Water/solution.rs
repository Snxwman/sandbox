use std::cmp::max;

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let mut left = 0;
        let mut right = height.len() - 1;
        let mut max_left = height[left];
        let mut max_right = height[right];
        let mut total = 0;

        if height.len() == 0 {
            return 0;
        }

        while left < right {
            if max_left < max_right || max_left == max_right {
                left += 1;
                max_left = max(max_left, height[left]);
                total += max_left - height[left];
            } else {
                right -= 1;
                max_right = max(max_right, height[right]);
                total += max_right - height[right];
            }
        }
        total
    }
}
