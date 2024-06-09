from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l,r = 0,len(height)-1
        maximum = 0
        while(l<r):
            h = min(height[l],height[r])
            b = r-l
            maximum = max(maximum, b*h)
            if height[l] < height[r]:
                l += 1
            else:# elif height[l] < height[r]:
                r -= 1
                
        return maximum
solution = Solution()
print(solution.maxArea([1,8,6,2,5,4,8,3,7]))