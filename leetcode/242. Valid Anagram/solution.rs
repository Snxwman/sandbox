impl Solution {

    pub fn is_anagram(s: String, t: String) -> bool {
        use std::collections::HashMap;

        if s.len() != t.len() {
            return false;
        }

        let mut freq: HashMap<char, i32> = HashMap::new();

        for (cs, ct) in s.chars().zip(t.chars()) {
            if cs != ct {
                match freq.get_mut(&cs) {
                    Some(v) => *v += 1,
                    None => {freq.insert(cs, 1);},
                }
                match freq.get_mut(&ct) {
                    Some(v) => *v -= 1,
                    None => {freq.insert(ct, -1);},
                }
            }
        }

        freq.iter().all(|(&k, &v)| v == 0)
    }
}
