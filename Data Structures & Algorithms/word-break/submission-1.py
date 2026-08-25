class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}

        def dfs(i):
            if i == len(s):
                return True
            
            if i in dp:return dp[i]

            for word in wordDict:
                if s[i:i+len(word)] == word:
                    next_idx = i + len(word)

                    if dfs(next_idx) == True:
                        dp[i] = True
                        return True
            dp[i] = False
            return False

        return dfs(0)

        