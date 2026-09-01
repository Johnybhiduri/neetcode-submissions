class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_count  = {}

        left  = 0
        right = 0
        max_window = 0
        while right < len(s):
            # Increase Char count of character
            if s[right] in char_count:
                char_count[s[right]] += 1
            else:
                char_count[s[right]] = 1

            # max replacement = window len - length of most freq char
            window_len = right - left + 1
            if window_len - max(char_count.values()) <= k:
                max_window  = max(window_len, max_window)
            
            else:
                char_count[s[left]] -= 1
                left += 1
            
            right += 1
            
        return max_window
