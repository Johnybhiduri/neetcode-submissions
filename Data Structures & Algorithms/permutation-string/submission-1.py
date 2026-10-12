from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        

        s1_char_count = Counter(s1)
        s2_counter = Counter(s2[:len(s1)])
        if s1_char_count == s2_counter:
            return True

        for i in range(1, len(s2)- len(s1)+1):
            s2_counter[s2[i-1]] -= 1
            s2_counter[s2[i+len(s1)-1]] += 1

            if s2_counter == s1_char_count:
                return True
        
        return False
