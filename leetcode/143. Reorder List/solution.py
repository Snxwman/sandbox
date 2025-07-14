# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: 'ListNode | None' = None):
        self.val: int = val
        self.next: ListNode | None = next


class Solution:
    # WARN: Do not return anything, modify head in-place instead.
    def reorderList(self, head: ListNode | None) -> None:
        if head is None:
            return

        slow: ListNode = head
        fast: ListNode | None = head.next
        # Find middle node
        while fast is not None and fast.next is not None:
            slow = slow.next  # pyright: ignore
            fast = fast.next.next

        cur_right_node = slow.next
        slow.next = None
        prev_right_node: ListNode | None = None

        # Reverse link direction of right half of linked list
        while cur_right_node is not None:
            next_right_node = cur_right_node.next
            cur_right_node.next = prev_right_node
            prev_right_node = cur_right_node
            cur_right_node = next_right_node

        # Splice left and right halfs
        left, right = head, prev_right_node
        while right is not None:
            orig_left_next = left.next  # pyright: ignore
            orig_right_next = right.next

            left.next = right
            right.next = orig_left_next

            left = left.next.next  # pyright: ignore
            right = orig_right_next
