from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

        # hashset = set()

        # for n in nums:
        #     if n in hashset:
        #         return True
        #     hashset.add(n)
        # return False
    

        # dictionary = {}
        # for i in range(len(nums)):
        #     dictionary[nums[i]] = 0
        # print(dictionary)
        # for i in range(len(nums)):
        #     dictionary[nums[i]] += 1
        #     print(dictionary)
        #     if dictionary[nums[i]] >= 2:
        #         return True
        # return False
solution = Solution()
result = solution.containsDuplicate([1,3,3,4,2])
print(result)