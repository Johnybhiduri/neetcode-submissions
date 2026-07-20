class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        longest  = 0
        for num in nums:
            if (num - 1) not in nums: # O(1) lookup
                length = 1
                current = num
                while (current + 1) in nums:
                    length += 1
                    current += 1
                
                longest  = max(longest, length)
        
        return longest