class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        def dfs(i, j):
            if (i, j) in visited: return
            visited.add((i, j))            
            dirs = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for x, y in dirs:
                if 0 <= x <m and 0 <= y <n and image[x][y] == image[i][j]:                    
                    dfs(x, y)  
            image[i][j] = color         
                
        m, n = len(image), len(image[0])
        if image[sr][sc] == color:
            return image
        visited = set()
        dfs(sr, sc)
        return image
        