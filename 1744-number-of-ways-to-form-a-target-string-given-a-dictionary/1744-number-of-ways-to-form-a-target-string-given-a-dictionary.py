class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1639.Number%20of%20Ways%20to%20Form%20a%20Target%20String%20Given%20a%20Dictionary
        @cache
        def dfs(i: int, j: int) -> int:
            if i >= m:
                return 1
            if j >= n:
                return 0
            ans = dfs(i + 1, j + 1) * cnt[j][ord(target[i]) - ord('a')]
            ans = (ans + dfs(i, j + 1)) % mod
            return ans

        m, n = len(target), len(words[0])
        cnt = [[0] * 26 for _ in range(n)]
        for w in words:
            for j, c in enumerate(w):
                cnt[j][ord(c) - ord('a')] += 1
        mod = 10**9 + 7
        return dfs(0, 0)
