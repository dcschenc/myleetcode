class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m, n = len(img), len(img[0])
        new_img = [[0 for j in range(n)] for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                # moves = [(i+1, j), (i-1, j), (i, j-1), (i, j+1), (i+1, j+1), (i-1, j-1), (i-1, j+1), (i+1, j-1)]
                total = 0
                cnt = 0
                # for x, y in moves:
                #     if 0 <= x <= m-1 and 0 <= y <= n-1:
                #         total += img[x][y]
                #         cnt += 1
                # total += img[i][j]
                # cnt += 1
                for x in (i-1, i, i + 1):
                    for y in (j-1, j, j + 1):
                        if 0 <= x < m and 0 <= y < n:
                            total += img[x][y]
                            cnt += 1

                new_img[i][j] = total // cnt
        return new_img
