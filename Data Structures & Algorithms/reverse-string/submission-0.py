class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        left  = 0
        right  = len(s)-1
        while  left  < right:
            s_left = s[left]
            s_right = s[right]

            s[left] = s_right
            s[right] = s_left

            left += 1
            right -= 1
        
        