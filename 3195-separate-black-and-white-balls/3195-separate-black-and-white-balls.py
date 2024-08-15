class Solution:
    def minimumSteps(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2938.Separate%20Black%20and%20White%20Balls
        n = len(s)
        ans = cnt = 0
        for i in range(n - 1, -1, -1):
            if s[i] == '1':
                cnt += 1
                ans += n - i - cnt
        return ans