from collections import defaultdict, Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t) # Count the required characters
        window = defaultdict(int) # Current window starts empty.
        required = len(need)  # Number of distinct characters required.
        formed = 0 # Number of requirements currently satisfied.

        left = 0 # Window boundaries.

        # Best answer found so far.
        best_start = 0
        best_len = float("inf")

        for right in range(len(s)):
            ch = s[right] # Get char


            # Increase its count in window.
            window[ch] += 1

            if ch in need and window[ch] == need[ch]:
                formed += 1
            
            while formed == required:
                # Find the length of the current window.
                current_len = right - left + 1

                if current_len < best_len:
                    best_len = current_len
                    best_start = left

                # get char leaving the window
                out = s[left]

                if out in need:
                    if window[out] == need[out]:
                        formed = formed - 1
                
                window[out] -= 1

                # Shrink the window from the left.
                left = left + 1

        if best_len == float("inf"):
            return ""
        
        return s[best_start: best_start+ best_len]
        


