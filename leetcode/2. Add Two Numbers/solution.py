class ListNode:
    def __init__(self, val: int=0, next: '(ListNode | None)'=None):
        self.val: int = val
        self.next: '(ListNode | None)' = next


class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        head = ListNode()
        cur = head
        carry = 0

        while l1 or l2 or carry:
            sum = carry

            if l1 is not None:
                sum += l1.val
                l1 = l1.next

            if l2 is not None:
                sum += l2.val
                l2 = l2.next

            carry = sum // 10
            cur.next = ListNode(sum % 10)
            cur = cur.next

        return head.next


    def addTwoNumbers_2(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        if l1 is None or l2 is None:
            return None


        def parse_num(node: ListNode) -> int:
            num: int = 0
            order: int = 0

            n = node
            while n is not None:
                num += n.val * (10 ** order)
                order += 1
                n = n.next

            return num


        def to_list(num: int) -> ListNode:
            digits = str(num)

            head = ListNode(int(digits[-1]))
            n = head
            for digit in digits[:-1][::-1]:
                n.next = ListNode(int(digit))
                n = n.next

            return head


        return to_list(parse_num(l1) + parse_num(l2))
