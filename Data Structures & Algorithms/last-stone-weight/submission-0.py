import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)

        while heap:
            if len(heap) > 1:
                largest, second_largest = -heapq.heappop(heap), -heapq.heappop(heap)
                if largest > second_largest:
                    new_val = largest-second_largest
                    heapq.heappush(heap, -new_val)

            else:
                return -heapq.heappop(heap)
        
        return 0