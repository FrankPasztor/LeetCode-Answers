from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult = 1
        r_mult = 1
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n

        for i in range(n):    #  1  2  3  4
            j = -i - 1        #  i -->
            l_arr[i] = l_mult #       <-- j
            r_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]
        
        return [l*r for l,r in zip(l_arr, r_arr)]

        # res = [1] * (len(nums)) #makes a list filled with 1s at the length of nums
        # prefix = 1
        # for i in range(len(nums)):
        #     res[i] = prefix
        #     prefix *= nums[i]
        # postfix = 1
        # for i in range(len(nums) - 1, -1, -1): #loops through the length of nums backwards
        #     res[i] *= postfix
        #     postfix *= nums[i]
        # return res
solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))