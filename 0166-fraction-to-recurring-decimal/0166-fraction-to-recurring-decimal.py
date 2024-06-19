class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/0100-0199/0166.Fraction%20to%20Recurring%20Decimal
        if numerator == 0:
            return '0'
        res = []
        if (numerator > 0) ^ (denominator > 0):
            res.append('-')
        num, d = abs(numerator), abs(denominator)
        res.append(str(num // d))
        num %= d
        if num == 0:
            return ''.join(res)
        res.append('.')
        mp = {}
        while num != 0:
            mp[num] = len(res)
            num *= 10
            res.append(str(num // d))
            num %= d
            if num in mp:
                idx = mp[num]
                res.insert(idx, '(')
                res.append(')')
                break
        return ''.join(res)        