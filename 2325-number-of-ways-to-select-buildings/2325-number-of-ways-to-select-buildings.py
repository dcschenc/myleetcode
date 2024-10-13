class Solution:
    def numberOfWays(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2222.Number%20of%20Ways%20to%20Select%20Buildings
        n = len(s)
        total_0 = s.count("0")
        total_1 = n - total_0
        c0 = c1 = 0
        ans = 0
        for c in s:
            if c == "0":
                ans += c1 * (total_1 - c1)
                c0 += 1
            else:
                ans += c0 * (total_0 - c0)
                c1 += 1
        return ans
