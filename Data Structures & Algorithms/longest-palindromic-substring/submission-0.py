class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        res = ""
        resLen = 0

        def longest_pal(l, r):
            nonlocal res
            nonlocal resLen

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l +1) > resLen:
                    res = s[l : r+1]
                    resLen = r-l+1
                
                l-=1
                r+=1
        
        for i in range(len(s)):
            l,r = i,i
            longest_pal(l,r) # odd

            l,r = i , i + 1
            longest_pal(l,r)
        
        return res