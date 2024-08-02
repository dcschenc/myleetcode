class Solution:
    def numberOfWays(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2222.Number%20of%20Ways%20to%20Select%20Buildings
        n = len(s)
        cnt0 = s.count("0")
        cnt1 = n - cnt0
        c0 = c1 = 0
        ans = 0
        for c in s:
            if c == "0":
                ans += c1 * (cnt1 - c1)
                c0 += 1
            else:
                ans += c0 * (cnt0 - c0)
                c1 += 1
        return ans
        
        # n = len(s)
        # pre0, pre1 = [0] * (n + 1), [0] * (n + 1)
        # pre01, pre10 = [0] * (n + 1), [0] * (n + 1)
        # i = n - 1
        # while i >= 0:
        #     if s[i] == '0':
        #         pre01[i] = pre01[i + 1] + pre1[i + 1]
        #         pre10[i] = pre10[i + 1]

        #         pre0[i] = pre0[i + 1] + 1
        #         pre1[i] = pre1[i + 1]
        #     else:
        #         pre10[i] = pre10[i + 1] + pre0[i + 1]
        #         pre01[i] = pre01[i + 1]

        #         pre0[i] = pre0[i + 1]
        #         pre1[i] = pre1[i + 1] + 1
        #     i -= 1
        # ans = 0
        # for i, c in enumerate(s):
        #     if c == '0':
        #         ans += pre10[i]
        #     else:
        #         ans += pre01[i]
        # return ans