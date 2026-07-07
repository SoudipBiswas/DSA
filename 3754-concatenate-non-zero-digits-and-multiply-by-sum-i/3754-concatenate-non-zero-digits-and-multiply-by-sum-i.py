class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = 0
        digit_sum = 0
        
        for char in str(n):
            if char != '0':
                digit = int(char)
                digit_sum += digit
                x = x * 10 + digit
                
        return x * digit_sum
