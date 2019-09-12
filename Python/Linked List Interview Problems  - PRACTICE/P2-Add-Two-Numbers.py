# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = curr = ListNode(0)
        p1, p2 = l1, l2
        carry = 0
        while carry or p1 or p2:
            if p1:
                carry += p1.val
                p1 = p1.next
            if p2:
                carry += p2.val
                p2 = p2.next

            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next


        return start.next
        
