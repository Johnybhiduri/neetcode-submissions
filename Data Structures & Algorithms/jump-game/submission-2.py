class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        for i in range(len(nums)):
            if i > max_idx:
                return False

            if max_idx >= len(nums) - 1:
                return True
            
            reach = i + nums[i]
            max_idx = max(max_idx, reach)
        
        return False