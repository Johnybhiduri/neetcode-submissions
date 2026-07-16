class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sorted_s = sorted(list(s))
        sorted_t  = sorted(list(t))

        if sorted_s == sorted_t:
            return True
        
        return False