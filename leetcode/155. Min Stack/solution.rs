use std::cmp::min;

struct MinStack {
    vals: Vec<(i32, i32)>,
    len: usize,
}


/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MinStack {

    fn new() -> Self {
        Self {
            vals: Vec::new(),
            len: 0,
        }
    }

    fn push(&mut self, val: i32) {
        if let Some(i) = self.vals.get(self.len - 1) {
            self.vals.push((val, min(val, i.1)));
        } else {
            self.vals.push((val, val));
        }
        self.len += 1;
    }

    fn pop(&mut self) {
        self.vals.remove(self.len - 1);
        self.len -= 1;
    }

    fn top(&self) -> i32 {
        self.vals.get(self.len - 1).unwrap().0.to_owned()
    }

    fn get_min(&self) -> i32 {
        self.vals.get(self.len - 1).unwrap().1.to_owned()
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * let obj = MinStack::new();
 * obj.push(val);
 * obj.pop();
 * let ret_3: i32 = obj.top();
 * let ret_4: i32 = obj.get_min();
 */
