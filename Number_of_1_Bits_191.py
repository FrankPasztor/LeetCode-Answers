class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= (n - 1)
            count += 1
        return count
    
        # total = 0
        # string = ""
        # while n > 0:
        #     string += str(n%2)
        #     n //= 2
        # # print(string)
        # for i in range(len(string)):
        #     if string[i] == "1":
        #         total += 1
        # return total
        
solution = Solution()
print(solution.hammingWeight(11))