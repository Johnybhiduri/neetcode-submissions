"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda interval: interval.start)
        required_rooms = []

        for interval in intervals:
            start = interval.start
            end = interval.end

            if not required_rooms:
                heapq.heappush(required_rooms, end)
                continue
            
            if required_rooms[0] <= start:
                heapq.heappop(required_rooms)  
            
            heapq.heappush(required_rooms, end)
        

        return len(required_rooms)

            
