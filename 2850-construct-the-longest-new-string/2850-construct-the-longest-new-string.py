class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2700-2799/2745.Construct%20the%20Longest%20New%20String
        if x < y:
            return (x * 2 + z + 1) * 2
        if x > y:
            return (y * 2 + z + 1) * 2
        return (x + y + z) * 2
