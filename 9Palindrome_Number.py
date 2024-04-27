class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0): return False
        
        div = 1
        while (x >= 10*div): 
            div *= 10

        while x: 
            first_num = x % 10
            second_num = x // div
            if (first_num != second_num): return False

            x %= div
            x //= 10
            div/=100
                
        return True
