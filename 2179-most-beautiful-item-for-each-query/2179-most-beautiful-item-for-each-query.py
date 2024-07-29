class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2070.Most%20Beautiful%20Item%20for%20Each%20Query
        items.sort()
        n, m = len(items), len(queries)
        ans = [0] * len(queries)
        i = mx = 0
        for q, j in sorted(zip(queries, range(m))):
            while i < n and items[i][0] <= q:
                mx = max(mx, items[i][1])
                i += 1
            ans[j] = mx
        return ans


        n = len(queries)
        ans = [0] * n
        items.sort(key=lambda x: (x[0], x[1]))
        mx = -1
        for i in range(len(items)):
            mx = max(mx, items[i][1])
            items[i][1] = mx
        prices = [p for p, b in items]
        for i, q in enumerate(queries):
            idx = bisect_right(prices, q)
            if idx - 1 >= 0:
                ans[i] = items[idx-1][1]
        return ans
