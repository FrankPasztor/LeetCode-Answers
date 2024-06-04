from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        start = 0
        end = len(nums) - 1
        

        while (start <= end):
            if nums[start] < nums[end]:
                res = min(res, nums[start])
                break
            middle = (start + end) // 2
            
            res = min(res, nums[middle])

            if nums[middle] >= nums[start]:
                start = middle + 1    
            else:
                end = middle - 1
        return res
    

# solution = Solution()
# result = solution.findMin([4,5,6,7,0,1,2])
# print(result)