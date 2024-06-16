from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # [12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
        dp[0] = 0 # [0, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
        # first loop in comments
        for a in range(1, amount + 1): # 1 or [0, (12), 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
            for c in coins: # [(1), 2, 5]
                if a - c >= 0: # 1 - 1 >= 0 (true)
                    dp[a] = min(dp[a], 1 + dp[a-c]) # [0, min(12, 1) = 1, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12]
        
        return dp[amount] if dp[amount] != amount + 1 else -1
solution = Solution()
print(solution.coinChange([1,2,5],11))