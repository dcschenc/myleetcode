class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2260.Minimum%20Consecutive%20Cards%20to%20Pick%20Up
        last = {}
        ans = inf
        for i, x in enumerate(cards):
            if x in last:
                ans = min(ans, i - last[x] + 1)
            last[x] = i
        return -1 if ans == inf else ans

        # hm = defaultdict(int)
        # ans, l, n = len(cards) + 1, 0, len(cards)
        # for i in range(n):
        #     if cards[i] in hm and l <= hm[cards[i]]:                
        #         ans = min(ans, i - hm[cards[i]] + 1)
        #         l = hm[cards[i]] + 1
        #     hm[cards[i]] = i
        # return ans if ans != n + 1 else -1