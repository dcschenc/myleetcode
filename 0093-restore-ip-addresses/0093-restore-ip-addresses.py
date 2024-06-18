class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def is_valid(start, end):
            if s[start] == '0' and start != end: return False
            if int(s[start: end + 1]) > 255: return False
            return True

        def backtrack(start, seg, path):
            if start == n:
                if seg == 4:
                    res.append(path[:-1])
                return
            if seg >= 4:
                return
            for i in range(start, n):
                if is_valid(start, i):
                    backtrack(i + 1, seg + 1, path + s[start:i + 1] + '.')          
            
        n, res = len(s), []
        backtrack(0, 0, '')
        return res

        def check(i: int, j: int) -> int:
            if s[i] == "0" and i != j:
                return False
            return 0 <= int(s[i : j + 1]) <= 255

        def dfs(i: int):
            if i >= n and len(t) == 4:
                ans.append(".".join(t))
                return
            if i >= n or len(t) >= 4:
                return
            for j in range(i, min(i + 3, n)):
                if check(i, j):
                    t.append(s[i : j + 1])
                    dfs(j + 1)
                    t.pop()

        n = len(s)
        ans = []
        t = []
        dfs(0)
        return ans
