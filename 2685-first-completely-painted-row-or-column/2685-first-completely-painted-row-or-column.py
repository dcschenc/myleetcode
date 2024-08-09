class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2661.First%20Completely%20Painted%20Row%20or%20Column
        m, n = len(mat), len(mat[0])
        hm = {}
        for r in range(m):
            for c in range(n):
                hm[mat[r][c]] = (r, c)
        row, col = Counter(), Counter()
        for i in range(len(arr)):
            r, c = hm[arr[i]]
            row[r] += 1
            col[c] += 1
            if row[r] == n or col[c] == m:
                return i
            