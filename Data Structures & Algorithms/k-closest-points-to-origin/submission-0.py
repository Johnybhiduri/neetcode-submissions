import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            distance = point[0]**2 + point[1]**2
            if len(max_heap) < k:
                heapq.heappush(max_heap, (-distance, point))
            else:
                max_dis = -max_heap[0][0]
                if distance < max_dis:
                    heapq.heappop(max_heap)
                    heapq.heappush(max_heap, (-distance, point))
        
        result = []
        for item in max_heap:
            result.append(item[1])
        
        return result
