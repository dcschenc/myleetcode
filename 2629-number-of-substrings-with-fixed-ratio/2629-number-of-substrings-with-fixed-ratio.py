class Solution:
    def fixedRatio(self, s: str, num1: int, num2: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2489.Number%20of%20Substrings%20With%20Fixed%20Ratio
        n = len(s)
        one, zero = 0, 0
        ans, cnt = 0, Counter({0: 1})
        for i, num in enumerate(s):
            if s[i] == '0':
                zero += 1
            else:
                one += 1
            x = one * num1 - zero * num2
            ans += cnt[x]
            cnt[x] += 1
        return ans
            