# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # create Dummy ListNode
        dummy = ListNode()
        result = dummy
        carry = 0
        while l1 or l2:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total = l1_val + l2_val + carry

            digit = total % 10
            carry = total // 10

            new_node = ListNode(val=digit)
            result.next = new_node

            l1 = l1.next if l1 else l1
            l2 = l2.next if l2 else l2

            result = result.next
        
        if carry:
            last_node = ListNode(val=carry)
            result.next = last_node
        
        return dummy.next
        