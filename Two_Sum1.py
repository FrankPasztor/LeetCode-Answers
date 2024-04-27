class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictionary = {}
        for i in range(len(nums)):
            goal = target - nums[i]
            if goal in dictionary and dictionary[goal] != i:
                return [dictionary[goal] , i]
            dictionary[nums[i]] = i
        return nums