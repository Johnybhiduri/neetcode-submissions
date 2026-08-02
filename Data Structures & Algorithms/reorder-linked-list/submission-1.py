# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def reverse_ll(node):
            prev = None
            current = node

            while current:
                nxt = current.next
                current.next = prev
                prev = current
                current = nxt
            
            return prev
        
        slow  = head
        fast = head.next

        while fast:
            slow = slow.next
            if fast.next:
                fast = fast.next.next
            else:
                break

        next_half = slow.next
        slow.next = None

        next_half_reversed = reverse_ll(next_half)

        first = head
        second = next_half_reversed

        while second:
            first_nxt = first.next
            second_nxt = second.next
            first.next = second
            second.next = first_nxt

            second = second_nxt
            first = first_nxt
        

           
