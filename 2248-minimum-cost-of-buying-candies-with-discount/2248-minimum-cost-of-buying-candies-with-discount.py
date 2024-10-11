class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        return sum(cost) - sum(cost[2::3])
        
        cost.sort(reverse=True)
        i, n, ans = 0, len(cost), 0
        while i < n:
            ans += cost[i]
            i += 1
            if i < n:
                ans += cost[i]
            i += 1
            if i < n:
                i += 1
        return ans