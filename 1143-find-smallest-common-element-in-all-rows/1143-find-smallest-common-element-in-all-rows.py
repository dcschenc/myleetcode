class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1198.Find%20Smallest%20Common%20Element%20in%20All%20Rows
        cnt = Counter()
        for row in mat:
            for x in row:
                cnt[x] += 1
                if cnt[x] == len(mat):
                    return x
        return -1

        m, n = len(mat), len(mat[0])
        hm = defaultdict(int)
        mx = -1
        for i in range(m):
            for j in range(n):
                hm[mat[i][j]] += 1
                mx = max(mx, mat[i][j])
        for i in range(1, mx + 1):
            if i in hm and hm[i] == m:
                return i
        return -1