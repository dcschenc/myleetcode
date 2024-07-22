class Solution:
    def countVowelStrings(self, n: int) -> int:
        def dfs(idx, level):
            if idx == n:
                ans[0] += 1
                return
            for i, c in enumerate('aeiou'):
                if i < level: continue
                dfs(idx + 1, i)
        ans = [0]
        dfs(0, 0)
        return ans[0]
