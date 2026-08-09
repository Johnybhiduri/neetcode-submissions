class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        prev = intervals[0]
        overlaps = 0

        for i in range(1, len(intervals)):
            current = intervals[i]
            # No overlap
            if prev[1] <= current[0]:
                prev  = current
            
            else:
                overlaps += 1
                if current[1] < prev[1]:
                    prev = current
            
        return overlaps