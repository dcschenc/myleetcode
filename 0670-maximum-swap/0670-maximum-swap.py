class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        i, n = 0, len(digits)
        for i in range(n):
            mx, idx = digits[i], -1
            for j in range(i+1, n):
                if mx <= digits[j]:
                    mx = digits[j]
                    idx = j
                mx = max(mx, digits[j])
            if mx != digits[i]:
                digits[i], digits[idx] = digits[idx], digits[i]
                return int(''.join(digits))
        return num