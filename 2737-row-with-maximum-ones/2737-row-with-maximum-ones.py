class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        ans = [0, mat[0].count(1)]
        for i in range(1, m):
            if mat[i].count(1) > ans[1]:
                ans = [i, mat[i].count(1)]
        return ans