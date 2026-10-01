class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(nums, left, mid, right):
            temp = []
            i = left
            j = mid + 1

            while i <= mid and j <= right:
                if nums[i] <= nums[j]:
                    temp.append(nums[i])
                    i+=1
                else:
                    temp.append(nums[j])
                    j+=1
                
            while i <= mid:
                temp.append(nums[i])
                i+=1
            
            while j <= right:
                temp.append(nums[j])
                j+=1

            for i in range(len(temp)):
                nums[left+i] = temp[i]
            


        def mergeSort(nums, left, right):
            if left >= right:
                return
            
            mid = (left+right) // 2

            mergeSort(nums, left, mid)
            mergeSort(nums, mid+1, right)

            merge(nums,left,mid, right)
        
        mergeSort(
                nums,
                0,
                len(nums) - 1
            )
        
        return nums
