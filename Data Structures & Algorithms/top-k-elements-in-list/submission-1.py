class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """top k frequent using bucket sort to get it done in o(n) instead of o(n log n)"""
        count  = {} # {num: number of times in nums}
        freq = [[] for i in range(len(nums) + 1)] # save num at index on how many times it appeared

        for num in nums:
            count[num] = count.get(num, 0) + 1
            
        for n, c in count.items():
            freq[c].append(n) # [[2,3],[1]] - 2 and 3 appeared 1 time and 1 appeared 2 times
        
        # iterate in desending order of the freq
        result = []
        for i in range(len(freq) - 1, 0, -1):
            result.extend(freq[i])
            if len(result) == k:
                return result
            
    
    