class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = list(set(nums))
        nums.sort()
        output = 1
        longest_seq = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                longest_seq += 1
                if longest_seq > output:
                    output = longest_seq
            else:
                if longest_seq > output:
                    output = longest_seq

                longest_seq = 1
        
        return output