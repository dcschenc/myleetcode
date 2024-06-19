class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, cur, path):
            if cur > n:
                return
            if len(path) == k:
                if cur == n:
                    ans.append(path[:])
                return
            for i in range(start + 1, 10):
                backtrack(i, cur + i, path + [i])
        ans = []
        backtrack(0, 0, [])
        return ans
