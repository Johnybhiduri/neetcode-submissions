class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest  = 0
        left = 0
        right = 0
        current = set()
        while right < len(s):
            if s[right] in current:
                while s[right] in current:
                    current.remove(s[left])
                    left+=1
                
            else:
                current.add(s[right])
                longest = max(longest, len(current))
                right += 1
                
        
        return longest
        