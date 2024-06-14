class Solution: 
    def climbStairs(self, n: int) -> int: # DP (dynamic programming problem)
        one, two = 1, 1 # counting the number of ways to get to the last step
        
        for i in range(n-1): # (0 -> n-1) [to count for the first two steps at 1 on line 3] 
            temp = one # temporary variable to hold the value of one for replacing two variable
            one = one + two # fibonacci sequence is used for calculating the possible outcomes from each step (current step (one) previous step (two))
            two = temp 

        return one
solution = Solution()
print(solution.climbStairs(5))
# (2)
# 1 + 1
# 2

# (3)
# 1 + 1 + 1
# 1 + 2
# 2 + 1

#(4)
# 1 + 1 + 1 + 1
# 1 + 1 + 2
# 2 + 1 + 1
# 2 + 2
# 1 + 2 + 1

#(5)
# 1 + 1 + 1 + 1 + 1 = 5
# 1 + 1 + 1 + 2 = 5
# 2 + 1 + 1 + 1 = 5
# 1 + 2 + 1 + 1 = 5
# 1 + 1 + 2 + 1 = 5
# 1 + 2 + 2 = 5
# 2 + 2 + 1 = 5
# 2 + 1 + 2 = 5
# n = 5 
