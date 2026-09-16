import heapq

class MedianFinder:

    def __init__(self):
        self.small_half = [] # Max heap
        self.large_half = [] # Min heap

    def addNum(self, num: int) -> None:
        if self.small_half:
            largest_small = -self.small_half[0]
        else:
            largest_small = float("-inf")

        if not self.small_half :
            heapq.heappush(self.small_half, -num) # Need to make num negative  to make a max heap as no max heap in python  
        elif num <= largest_small:
            heapq.heappush(self.small_half, -num)

        else:
            heapq.heappush(self.large_half, num)
        
        if len(self.small_half) + 1 > len(self.large_half):
            largest = -heapq.heappop(self.small_half)
            heapq.heappush(self.large_half, largest)
        
        if len(self.large_half) > len(self.small_half):
            smallest = heapq.heappop(self.large_half)
            heapq.heappush(self.small_half, -smallest)

    def findMedian(self) -> float:
        
        if len(self.small_half) == len(self.large_half) + 1:
            return -self.small_half[0]
        
        else:
            mid1 = -self.small_half[0]
            mid2 =self.large_half[0]

            return (mid1 + mid2)/2