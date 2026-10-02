class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Brute Force approach

        # step 1: create prefixes for smallest str in strs -> bad, ba, b  longest to smallest
        smallest_str:Optional[str] = None 
        for s in strs:
            if smallest_str:
                if len(s) < len(smallest_str):
                    smallest_str = s
            else:
                smallest_str = s
        
        prefixes = []
        if smallest_str:
            for i in range(len(smallest_str)):
                prefixes.append(smallest_str[: len(smallest_str) - i])

        else:
            return ""

        
        # step 2: check all strs to for common prefix
        result = ''
        for prefix in prefixes:
            match_count = 0
            for s in strs:
                if s[: len(prefix)] == prefix:
                    match_count += 1
            
            if match_count == len(strs):
                result = prefix
                break
        
        return result