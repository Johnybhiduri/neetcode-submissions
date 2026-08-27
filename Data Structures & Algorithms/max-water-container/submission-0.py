class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_res = 0
        left = 0
        right = len(heights)-1

        while left < right:
            dis = right - left
            height = min(heights[left], heights[right])
            max_res = max(max_res, dis * height)

            if heights[left] > heights[right]:
                right -= 1
            elif heights[left] < heights[right]:
                left  += 1
            else:
                right -= 1
                left += 1
        
        return max_res
            