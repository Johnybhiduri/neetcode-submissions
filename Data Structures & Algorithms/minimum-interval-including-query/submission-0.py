class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        queries_with_index = []
        for i, q in enumerate(queries):
            queries_with_index.append((q,i))

        sorted_queries = sorted(queries_with_index, key=lambda x: x[0])
        
        output = [-1] * len(queries)
        heap = []
        i = 0

        for q, org_i in sorted_queries:
            while i < len(intervals) and sorted_intervals[i][0] <= q:
                length = (sorted_intervals[i][1] - sorted_intervals[i][0]) + 1
                heapq.heappush(heap, (length, sorted_intervals[i]))
                i+=1

            while heap:
                if heap[0][1][1] < q:
                    heapq.heappop(heap)
                else:
                    break
            
            if heap:
                output[org_i] = heap[0][0]
        
        return output