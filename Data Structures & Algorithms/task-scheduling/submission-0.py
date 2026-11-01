import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = []
        for k, v in counter.items():
            heapq.heappush(heap, -v)
        

        queue = deque()
        time = 0

        while heap or queue:
            time+=1
            
            if heap:
                cnt = 1  + heapq.heappop(heap)
                if cnt:
                    queue.append([cnt, time + n])
                
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])

        return time