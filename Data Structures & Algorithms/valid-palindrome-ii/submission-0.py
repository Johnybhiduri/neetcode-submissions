class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        for i in range(len(s)):
            chars = [c for  c in s]
            chars.pop(i)
            x = "".join(chars)
            if x == x[::-1]:
                return True
        
        return False