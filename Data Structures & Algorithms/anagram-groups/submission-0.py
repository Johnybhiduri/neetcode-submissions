class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for word in strs:
            chrs = list(word)
            chrs.sort()
            new = "".join(chrs)

            if new in anagrams:
                anagrams[new].append(word)
            
            else:
                anagrams[new] = [word]
        
        result = []
        for word in anagrams:
            result.append(anagrams[word])
        
        return result
    