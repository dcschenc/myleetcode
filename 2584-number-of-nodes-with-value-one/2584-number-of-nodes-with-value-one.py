class Solution:
    def numberOfNodes(self, n: int, queries: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2445.Number%20of%20Nodes%20With%20Value%20One
        queries = Counter(queries)
        ans = 0
        for i in range(n, -1, -1):
            cnt = 0
            j = i
            while j > 0:
                cnt += queries[j]
                j = math.floor(j / 2)
            if cnt % 2 == 1:
                ans += 1
        return ans