class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        digits = list(str(n))
        
        for i in range(len(digits)-1, -1, -1):
            if i-1 >= 0  and digits[i] < digits[i-1]:
                for j in range(i, len(digits)):
                    digits[j] = str(9)
                digits[i-1] = str(int(digits[i-1]) -1)
            # else:
                # break
        return int(''.join(digits))