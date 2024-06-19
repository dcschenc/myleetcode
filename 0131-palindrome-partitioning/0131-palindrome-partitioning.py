
class Solution:
    @cache
    def partition(self, s: str) -> List[List[str]]:    
        def dfs(i: int, path):
            if i == n:
                ans.append(path[:])
                return
            for j in range(i, n):
                if dp[i][j]:
                    # path.append(s[i : j + 1])
                    dfs(j + 1, path + [s[i:j+1]])
                    # path.pop()

        n = len(s)
        dp = [[True] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]
        ans = []
        # path = []
        dfs(0, [])
        return ans


        # def is_palindrome(s):           
        #     i, j = 0, len(s) - 1
        #     while i < j:
        #         if s[i] != s[j]:
        #             return False
        #         i += 1
        #         j -= 1
        #     return True

        # n = len(s)
        # res = []
        # for i in range(n):           
        #     if is_palindrome(s[:i+1]):
        #         if i == n-1:
        #             res.append([s])
        #         for p in self.partition(s[i+1:]):
        #             res.append([s[:i+1]] + p)                
        # # self.cached[s] = res
        # return res

        