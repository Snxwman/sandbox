impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        use std::collections::HashMap;

        let mut groups: Vec<(HashMap<char, u32>, Vec<String>)> = Vec::new();

        for string in strs {
            let mut freq: HashMap<char, u32> = HashMap::new();

            for c in string.chars() {
                freq.get_mut(&c)
                    .and_then(|v| Some(*v += 1))
                    .or_else(|| Some({freq.insert(c, 1);}));

                // match freq.get_mut(&c) {
                //     Some(v) => *v += 1,
                //     None => {freq.insert(c, 1);},
                // }
            }

            groups
                .iter_mut()
                .find(|group| &group.0 == &freq)
                .and_then(|group| Some(group.1.push(string.clone())))
                .or_else(|| Some(groups.push((freq.clone(), vec![string.clone()]))));
        }

        groups
            .into_iter()
            .map(|(_, v)| v)
            .collect()
    }
}
