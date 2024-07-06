class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1079.Letter%20Tile%20Possibilities
        def dfs(cnt: Counter) -> int:
            ans = 0
            for i, x in cnt.items():
                if x > 0:
                    ans += 1
                    cnt[i] -= 1
                    ans += dfs(cnt)
                    cnt[i] += 1
            return ans

        cnt = Counter(tiles)
        return dfs(cnt)

        def backtrack():
            nonlocal ans                   
            ans[0] += 1
            for i in range(n):
                if i > 0 and tiles[i] == tiles[i-1] and used[i-1] == False:
                    continue
                if used[i] == False:
                    used[i] = True
                    backtrack()
                    used[i] = False          
            
        ans = [0]
        tiles = sorted(tiles)
        n = len(tiles)
        used = [False] * n
        backtrack()
        return ans[0] - 1
            