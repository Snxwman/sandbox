impl Solution {
    pub fn is_valid(s: String) -> bool {
        let mut stack = Vec::new();

        for (i, ch) in s.chars().enumerate() {
            match ch {
                '(' | '[' | '{' => stack.push(ch),
                _ => {
                    let pch = match stack.pop() {
                        Some(c) => c,
                        None => return false,
                    };

                    if !(pch == '(' && ch == ')' || pch == '[' && ch == ']' || pch == '{' && ch == '}') {
                        return false;
                    }
                }
            }
        }

        match stack.pop() {
            Some(ch) => false,
            None => true,
        }
    }
}
