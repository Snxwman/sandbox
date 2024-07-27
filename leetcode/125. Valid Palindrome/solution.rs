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

    pub fn is_palindrome2(s: String) -> bool {
        let s: String = s
            .to_lowercase()
            .chars()
            .filter(|c| c.is_ascii_alphanumeric())
            .collect();

        for (c1, c2) in s.chars().zip(s.chars().rev()) {
            if c1 != c2 {
                return false;
            }
        }

        true
    }

    pub fn is_palindrome3(s: String) -> bool {
        s.to_lowercase()
            .chars()
            .filter(|c| c.is_ascii_alphanumeric())
            .zip(
                s.to_lowercase()
                    .chars()
                    .filter(|c| c.is_ascii_alphanumeric())
                    .rev()
            )
            .map(|(c1, c2)| {
                if c1 != c2 {
                    return false;
                }
                true
            })
            .all(|i| i == true)
    }

    pub fn is_palindrome4(s: String) -> bool {
        let s: String = s
            .to_lowercase()
            .chars()
            .filter(|c| c.is_ascii_alphanumeric())
            .collect();

        s.chars().eq(s.chars().rev())
    }
}
