class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        colors = colors * 2
        n = len(colors)
        total = 0
        for i in range(n // 2):
            if colors[i:i+3] == [0, 1, 0] or colors[i:i+3] == [1, 0, 1]:
                total += 1
        return total