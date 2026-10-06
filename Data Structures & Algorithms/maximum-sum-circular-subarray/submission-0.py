class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # Brute Force
        n = len(nums)
        max_sum = float('-inf')
        for i in range(n):
            current_sum = 0
            
            for j in range(1, n+1):
                index = (i+j-1) % n
                current_sum += nums[index]
                max_sum = max(max_sum, current_sum)
        
        return max_sum