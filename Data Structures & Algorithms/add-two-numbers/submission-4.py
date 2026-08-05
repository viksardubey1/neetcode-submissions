# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        carry = 0
        curr = dummy
        while l1 or l2 or carry:
            first_val = l1.val if l1 else 0
            second_val = l2.val if l2 else 0
            sum = first_val + second_val + carry
            curr.next = ListNode(val = sum % 10)
            carry = sum // 10
            curr = curr.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        return dummy.next



        