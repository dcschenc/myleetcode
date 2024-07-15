class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1300-1399/1383.Maximum%20Performance%20of%20a%20Team
        t = sorted(zip(speed, efficiency), key=lambda x: -x[1])
        ans = tot = 0
        mod = 10**9 + 7
        h = []
        for s, e in t:
            tot += s
            ans = max(ans, tot * e)
            heappush(h, s)
            if len(h) == k:
                tot -= heappop(h)
        return ans % mod