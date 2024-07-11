class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        # search in 8 directions
        n = 8
        dr = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        ans = []
        for dx, dy in dr:
            x, y = king
            while 0 <= x + dx < 8 and 0 <= y + dy < 8:
                x, y = x + dx, y + dy
                if [x, y] in queens:
                    ans.append([x, y])
                    break
        return ans
