# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int=0, next: 'ListNode | None'=None):
        self.val: int = val
        self.next: ListNode | None = next

class Solution:
    def getDecimalValue(self, head: ListNode | None) -> int:
        digits: list[int] = []

        node = head
        while node is not None:
            digits.append(node.val)
            node = node.next

        return sum([num*(2**i) for i, num in enumerate(digits[::-1])]) 
