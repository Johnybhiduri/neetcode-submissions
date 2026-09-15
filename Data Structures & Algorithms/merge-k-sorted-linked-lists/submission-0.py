# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        counter = 0
        for ls in lists:
            if ls:
                heapq.heappush(heap, (ls.val, counter, ls))
                counter += 1

        dummy = ListNode()
        tail = dummy
        while heap:
            smallest = heapq.heappop(heap)[-1]
            tail.next = smallest
            tail = smallest
            if smallest.next:
                heapq.heappush(heap, (smallest.next.val, counter, smallest.next))
                counter += 1
        
        return dummy.next