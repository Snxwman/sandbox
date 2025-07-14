# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val: int = val
        self.next: ListNode | None = next


class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        if head is None or head.next is None:
            return

        target_prev: ListNode | None = None
        target: ListNode = head
        tail: ListNode = head

        # Offset tail from target by n so target will point to the nth from last node
        for _ in range(n - 1):
            tail = tail.next  # pyright: ignore

        # Walk pointers to the end of the list
        while tail.next is not None:
            target_prev = target
            target = target.next  # pyright: ignore
            tail = tail.next

        # Removing first node
        if target_prev is None:
            return head.next

        target_prev.next = target.next
        return head
