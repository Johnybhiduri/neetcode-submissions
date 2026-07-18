class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Brute Force approach with O(n^2) time and space complexity"""

        output = []

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if j != i:
                    product = product * nums[j]

            output.append(product)
        
        return output