class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        def backtrack(cnt, path):
            if cnt == n:
                ans.append(path)
                return            
            for c in 'abc':
                if len(path) == 0 or path[-1] != c:
                    backtrack(cnt + 1, path + c)
        ans = []
        backtrack(0, '')
        return ans[k-1] if k -1 < len(ans) else ''
        