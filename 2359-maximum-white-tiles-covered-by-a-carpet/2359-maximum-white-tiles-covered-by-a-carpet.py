class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2271.Maximum%20White%20Tiles%20Covered%20by%20a%20Carpet
        tiles.sort()
        n = len(tiles)
        s = ans = j = 0
        for i, (l, r) in enumerate(tiles):
            while j < n and tiles[j][1] - l + 1 <= carpetLen:
                s += tiles[j][1] - tiles[j][0] + 1
                j += 1
            if j < n and l + carpetLen > tiles[j][0]:
                ans = max(ans, s + l + carpetLen - tiles[j][0])
            else:
                ans = max(ans, s)
            s -= r - l + 1
        return ans

      