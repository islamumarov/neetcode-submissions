# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        prev = slow

        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next

        slow = prev.next
        prev.next = None
        first = head
        second = self.reverse(slow)
        while first and second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            first = first_next
            second = second_next
        
    
    def reverse(self, head):
        prev = None
        cur = head

        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        return prev



