class Solution:
    def minimumCosts(self, regular: List[int], express: List[int], expressCost: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2361.Minimum%20Costs%20Using%20the%20Train%20Line
        n = len(regular)
        f = [0] * (n + 1)
        g = [inf] * (n + 1)
        cost = [0] * n
        for i, (a, b) in enumerate(zip(regular, express), 1):
            f[i] = min(f[i - 1] + a, g[i - 1] + a)
            g[i] = min(f[i - 1] + expressCost + b, g[i - 1] + b)
            cost[i - 1] = min(f[i], g[i])
        return cost
