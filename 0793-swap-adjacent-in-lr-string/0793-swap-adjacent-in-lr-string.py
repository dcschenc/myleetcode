class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/0700-0799/0777.Swap%20Adjacent%20in%20LR%20String
        n = len(start)
        i = j = 0
        while 1:
            while i < n and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1
            if i >= n and j >= n:
                return True
            if i >= n or j >= n or start[i] != end[j]:
                return False
            if start[i] == 'L' and i < j:
                return False
            if start[i] == 'R' and i > j:
                return False
            i, j = i + 1, j + 1

    