from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        if not self.timeMap.get(key):
            return ""
        
        values = self.timeMap[key]

        candidate = None
        left = 0
        right = len(values)-1
        while left <= right:
            mid = (left+right)//2
            mid_time= values[mid][0]
            if mid_time <=  timestamp:
                candidate = values[mid][1]
                left = mid + 1
            else:
                right = mid - 1

        if not candidate:
            return ""

        return candidate           
