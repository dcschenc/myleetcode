class Solution:
    def appealSum(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2262.Total%20Appeal%20of%20A%20String
        ans = t = 0
        # pos = [-1] * 26
        seen = {}
        for i, c in enumerate(s):
            c = ord(c) - ord('a')
            if c not in seen:
                t += i + 1
            else:
                t += i - seen[c]
            ans += t
            seen[c] = i
        return ans
