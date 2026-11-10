class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_time = []

        for pos, s in zip(position, speed):
            distance = target - pos
            time = distance/s
            pos_time.append((pos, time))
        
        pos_time_sorted = sorted(pos_time, key=lambda x: x[0], reverse=True)

        fleets = 0
        last_time = 0
        for item in pos_time_sorted:
            if item[1] > last_time:
                fleets += 1
                last_time = item[1]
        
        return fleets
