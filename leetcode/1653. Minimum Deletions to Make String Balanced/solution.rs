// Any instance of "ba" requires at least one deletion.
// There can be up to n additional required deletions where n is the minimum number of matched
// pairs of b's and a's on either side of the first found "ba" pair.
//
// From a stack perspective, you cannot push an 'a' after pushing a 'b'.
// If an 'a' is found while the top element of the stack is 'b', they *annihilate*
// (the 'b' is popped, and the 'a' is not pushed).
// Subsequent iterations of the loop will handle the recursive "ba" pairs.
//
// This might be able to be done with better memory efficiency by using two pointers that
// start at a "ba" pair and move out to get a count of the number of preceeding 'b's and
// succeeding 'a's, then adding the minimum of those two to the removal count.
impl Solution {
    pub fn minimum_deletions(s: String) -> i32 {
        let mut stack: Vec<char> = Vec::new();
        let mut removals = 0;

        for c in s.chars() {
            let last = stack.last().or(Some(&' ')).unwrap();
            if c == 'a' && *last == 'b' {
                removals += 1;
                stack.pop();
            } else {
                stack.push(c);
            }
        }

        removals
    }
}
