class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp = {}
        dp[0] = (nums[0], nums[0])

        for i in range(1, len(nums)):
            num = nums[i]
            prod1 = num * dp[i-1][0]
            prod2 = num * dp[i-1][1]
            max_prod  = max(prod1, prod2)
            min_prod  = min(prod1,prod2)

            dp[i] = (max(max_prod, num),min(min_prod, num))

        
        result  = float("-inf")
        for num_tup in dp.values():
            max_num_tup = max(num_tup)
            result = max(result, max_num_tup)
        
        return result