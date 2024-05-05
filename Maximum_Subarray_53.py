from typing import List
#find the subarray with the largest sumand return that sum
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum = 0
        for n in nums:
            if sum < 0:
                sum = 0
            sum += n
            max_sum = max(sum, max_sum)
        return max_sum
solution = Solution()
print(solution.maxSubArray([-2,-10,-3,-4,-1,-2,-1,-5,-4]))