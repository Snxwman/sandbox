impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let s_forwards: String = s
            .to_lowercase()
            .chars()
            .filter(|c| c.is_ascii_alphanumeric())
            .collect();

        let s_backwards: String = s_forwards.chars().rev().collect();

        s_forwards == s_backwards
    }
}
