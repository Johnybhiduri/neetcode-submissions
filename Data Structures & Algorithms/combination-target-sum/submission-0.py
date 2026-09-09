class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(start,  remaining, current):
            if remaining == 0:
                result.append(current.copy())
                return 
            
            if remaining < 0:
                return
            
            for i in range(start, len(nums)):
                num = nums[i]
                current.append(num)
                backtrack(i, remaining-num, current)

                current.pop()

        current = []
        backtrack(0,target,current) 

        return result       