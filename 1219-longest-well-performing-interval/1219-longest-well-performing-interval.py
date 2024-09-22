class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1124.Longest%20Well-Performing%20Interval
        ans = s = 0
        pos = {}
        for i, x in enumerate(hours):
            s += 1 if x > 8 else -1
            if s > 0:
                ans = i + 1
            elif s - 1 in pos:
                ans = max(ans, i - pos[s - 1])
            if s not in pos:
                pos[s] = i
        return ans