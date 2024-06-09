from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers)-1
        while (l<r):
            curSum = numbers[l] + numbers[r]
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l+1, r+1]

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         dictionary = {}
#         for i in range(len(numbers)):
#             goal = target - numbers[i]
#             if goal in dictionary and dictionary[goal] != i:
#                 return [dictionary[goal]+1 , i+1]
#             dictionary[numbers[i]] = i
#         return numbers
solution = Solution()
print(solution.twoSum([2,7,11,15],9))