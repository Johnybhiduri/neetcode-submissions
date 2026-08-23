class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {}

        def dfs(amount):
            if amount == 0:
                return 0
            
            if amount in dp:
                return dp[amount]
            
            best = float("inf")
            for coin in coins:
                if coin <= amount:
                    result = dfs(amount - coin)
                    if result is not None:
                        best = min(best, 1+ result)
            
            dp[amount] = best
            
            return best
        
        answer = dfs(amount)
        if answer == float("inf"):
            return -1
        
        return answer
        