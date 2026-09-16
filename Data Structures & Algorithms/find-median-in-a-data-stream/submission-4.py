import heapq

class MedianFinder:

    def __init__(self):
        self.small = [] # Keep smaller half with Max heap
        self.large = [] # Keep larger half with Min heap

    def addNum(self, num: int) -> None:
        if not self.small:
            heapq.heappush(self.small, -num)

        elif num <= -self.small[0]:
            heapq.heappush(self.small, -num)
        
        else:
            heapq.heappush(self.large, num)
        
        if len(self.small) + 1  > len(self.large):
            largest_in_small = -heapq.heappop(self.small)
            heapq.heappush(self.large, largest_in_small)

        if len(self.large) > len(self.small):
            samllest_in_large = heapq.heappop(self.large)
            heapq.heappush(self.small, -samllest_in_large)

    def findMedian(self) -> float:
        if len(self.small) == len(self.large) + 1:
            return -self.small[0]
        
        else:
            mid1 = -self.small[0]
            mid2 =self.large[0]

            return (mid1 + mid2)/2