class Solution:
    def rob(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return nums[0]

        def solve(houses:List[int]):
            if len(houses) == 1:
                return houses[0]

            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])

            current_max = 0
            for i in range(2, len(houses)):
                dp[i]  = max(dp[i-1], houses[i] + dp[i-2])
                
            return dp[-1]
        
        sol1 = solve(nums[: -1])
        sol2 = solve(nums[1 : ])

        return max(sol1,sol2)