class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n>>i) & 1 # Bitwise shift n value to the right i places, then logic and it with one. ()
            res = res | (bit <<  (31-i))
        return res
solution = Solution()
print(solution.reverseBits(0b00000010100101000001111010011100))