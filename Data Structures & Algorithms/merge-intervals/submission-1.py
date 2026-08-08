class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # step 1:  Sort the intervals with start time
        intervals.sort()

        # step 2: save first interval in the result
        result = [intervals[0]]

        #step 3: iterate over each next intervals
        for i in range(1,  len(intervals)):
            current_interval = intervals[i]
            prev_interval = result[-1]

            # step 4: if overlap then merge
            if current_interval[0] <= prev_interval[1]:
                prev_interval[1] = max(current_interval[1],prev_interval[1])
            
            else:
                result.append(current_interval)
        
        return result

