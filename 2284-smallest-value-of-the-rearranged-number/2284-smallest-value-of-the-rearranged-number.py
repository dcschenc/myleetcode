class Solution:
    def smallestNumber(self, num: int) -> int:
        digits = str(num)
        if len(digits) == 1:
            return num
            
        if digits[0] != '-':
            digits = [int(d) for d in digits]
            digits.sort()
            n, i = len(digits), 0
            while i < n:
                if digits[i] != 0:
                    break
                i += 1
            ans = str(digits[i])
            for j in range(n):
                if j != i:
                    ans += str(digits[j])
            return int(ans)
        else:
            digits = [int(d) for d in digits[1:]]
            digits.sort(reverse=True)
            return -int(''.join(str(d) for d in digits))
