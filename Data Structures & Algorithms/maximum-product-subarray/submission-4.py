class Solution:
    def maxProduct(self, nums: List[int]) -> int:
    
        prev_max, prev_min = nums[0], nums[0]
        answer = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            prod1 = num * prev_max
            prod2 = num * prev_min

            curr_max = max(prod1,prod2,num)
            curr_min = min(prod1,prod2,num)
            answer = max(answer, curr_max)

            prev_max,prev_min = curr_max,curr_min

        return answer