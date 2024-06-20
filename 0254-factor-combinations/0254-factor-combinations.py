class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        def backtrack(n, i):
            if path:
                ans.append(path + [n])
            j = i
            while j * j <= n:
                if n % j == 0:
                    path.append(j)
                    backtrack(n // j, j)
                    path.pop()
                j += 1

        path = []
        ans = []
        backtrack(n, 2)
        return ans