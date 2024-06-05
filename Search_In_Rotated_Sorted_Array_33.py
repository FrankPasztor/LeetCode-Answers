from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = nums[0]
        l = 0
        r = len(nums) - 1

        while (l <= r):
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1 
                else:
                    r = mid - 1   
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
    
solution = Solution()
print(solution.search([4,5,6,7,8,1,2,3],8))
            