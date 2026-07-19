class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """To solve this question we will first get product of each num with rest of them from the left then do same
        from right and mutliple with the left on the fly to get the answer."""


        output =  [1] * len(nums)
        left  = 1
        for i in range(len(nums)):
            output[i] = left
            left *= nums[i]
        
        right = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
        
        return output
        
        
        
        
