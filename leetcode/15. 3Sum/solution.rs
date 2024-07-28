impl Solution {
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort();

        let mut a_ptr = 0;
        let mut b_ptr = a_ptr + 1;
        let mut c_ptr = nums.len() - 1;

        let mut trips = Vec::new();

        while nums[a_ptr] <= 0 && a_ptr + 2 < nums.len() {
            let a = nums[a_ptr];

            while b_ptr < c_ptr {
                let b = nums[b_ptr];
                let c = nums[c_ptr];
                let sum = b + c;

                if a + sum < 0 {
                    b_ptr = next_unique_index(&nums, b_ptr, c_ptr);
                } else if a + sum > 0 {
                    c_ptr = prev_unique_index(&nums, c_ptr, b_ptr);
                } else if a + sum == 0 {
                    trips.push(vec![a.clone(), b.clone(), c.clone()]);
                    b_ptr = next_unique_index(&nums, b_ptr, c_ptr);
                }
            }

            a_ptr = next_unique_index(&nums, a_ptr, b_ptr);
            b_ptr = a_ptr + 1;
            c_ptr = nums.len() - 1;
        }

        trips
    }
}

fn next_unique_index(list: &Vec<i32>, cur_index: usize, max_index: usize) -> usize {
    let mut next_index = cur_index + 1;
    while list[next_index] == list[cur_index] && next_index < max_index {
        next_index += 1;
    }
    next_index
}

fn prev_unique_index(list: &Vec<i32>, cur_index: usize, min_index: usize) -> usize {
    let mut prev_index = cur_index - 1;
    while list[prev_index] == list[cur_index] && prev_index > min_index {
        prev_index -= 1;
    }
    prev_index
}
