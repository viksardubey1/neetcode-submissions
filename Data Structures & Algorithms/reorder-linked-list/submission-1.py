# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None

        prev = None
        while second:
            next_val = second.next
            second.next = prev
            prev = second
            second = next_val
        
        first = head
        second = prev
        while first and second:
            first_skip = first.next
            first.next = second
            first = first_skip
            second_skip = second.next
            second.next = first
            second = second_skip




        