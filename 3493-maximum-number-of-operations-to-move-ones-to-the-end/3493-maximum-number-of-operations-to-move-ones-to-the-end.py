class Solution:
    def maxOperations(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3200-3299/3228.Maximum%20Number%20of%20Operations%20to%20Move%20Ones%20to%20the%20End
        ans = cnt = 0
        for i, c in enumerate(s):
            if c == "1":
                cnt += 1
            elif i and s[i - 1] == "1":
                ans += cnt
        return ans