impl Solution {
    pub fn merge_two_lists(
        mut list1: Option<Box<ListNode>>,
        mut list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut head = None;
        let mut tail = &mut head;

        while list1.is_some() && list2.is_some() {
            let l1 = &mut list1;
            let l2 = &mut list2;

            let mut next = if l2.as_ref()?.val > l1.as_ref()?.val {
                l1
            } else {
                l2
            };

            std::mem::swap(tail, &mut next);
            std::mem::swap(next, &mut tail.as_mut()?.next);
            tail = &mut tail.as_mut()?.next;
        }

        std::mem::swap(tail, if list1.is_none() { &mut list2 } else { &mut list1 });
        head
    }
}
