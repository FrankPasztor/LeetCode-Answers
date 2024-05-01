from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        max_profit = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            else:
                l=r
            r+=1
        return max_profit
        # l = 0
        # max_profit = 0
        # for r in range(1,len(prices)):
        #     print(str(prices[l]) + " l vs r " + str(prices[r]))
        #     if prices[l] < prices[r]:
        #         if prices[r] - prices[l] > max_profit:
        #             max_profit = prices[r] - prices[l]
        #             minimum = prices[l]
        #     while prices[r] < prices[l]:
        #             l+=1
        # return max_profit
solution = Solution()
print(solution.maxProfit([1,2,11,2,5,7,2,40,9,0,20]))