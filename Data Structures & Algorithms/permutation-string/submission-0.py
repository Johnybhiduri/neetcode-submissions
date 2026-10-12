class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def check_substrings(s1, s2_cut):
            s1_sort = sorted(s1)
            s2_cut_sort = sorted(s2_cut)

            if  s1_sort == s2_cut_sort:
                return True
            
            return False

        s1_len = len(s1)
        for i in range(len(s2)-s1_len+1):
            if check_substrings(s1, s2[i:i+s1_len]):
                return True
        
        return False
        