class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        smallest = min(strs, key=len) # Get smallest word
        strs.remove(smallest)

        result = ''
        for i in range(len(smallest)):
            char = smallest[i]
            stop = False
            for s in strs:
                if s[i] != char:
                    stop = True
                    break

            if stop:
                break

            result += char

        return result
            
