class Solution:
    def appealSum(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2262.Total%20Appeal%20of%20A%20String
        ans = t = 0
        pos = [-1] * 26
        for i, c in enumerate(s):
            c = ord(c) - ord('a')
            t += i - pos[c]
            ans += t
            pos[c] = i
        return ans
