class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3200-3299/3208.Alternating%20Groups%20II
        n = len(colors)
        ans = cnt = 0
        for i in range(n << 1):
            if i and colors[i % n] == colors[(i - 1) % n]:
                cnt = 1
            else:
                cnt += 1
            ans += i >= n and cnt >= k
        return ans