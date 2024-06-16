from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums)-1,-1,-1): # for (int i = nums.length-1; i > -1; i--){}
            for j in range(i+1,len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
solution = Solution()
print(solution.lengthOfLIS([10,9,2,5,3,7,101,18]))