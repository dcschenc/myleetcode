class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:        
        def backtrack(start, cnt, path):
            if cnt == k:
                ans.append(path[:])
                return
            for i in range(start + 1, n + 1):
                backtrack(i, cnt + 1, path + [i])

        ans = []
        backtrack(0, 0, [])
        return ans