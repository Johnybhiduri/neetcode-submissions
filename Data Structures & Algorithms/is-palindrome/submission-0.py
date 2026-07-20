class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_combined = "".join(ch for ch in s if ch.isalnum())
        s_combined = s_combined.lower()

        return s_combined == s_combined[:: -1]