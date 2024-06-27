class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        # n = len(start)
        # i = j = 0
        # while 1:
        #     while i < n and start[i] == 'X':
        #         i += 1
        #     while j < n and end[j] == 'X':
        #         j += 1
        #     if i >= n and j >= n:
        #         return True
        #     if i >= n or j >= n or start[i] != end[j]:
        #         return False
        #     if start[i] == 'L' and i < j:
        #         return False
        #     if start[i] == 'R' and i > j:
        #         return False
        #     i, j = i + 1, j + 1

        a, b = [], []
        for i, c in enumerate(start):
            if c != 'X':
                a.append((c, i))
        for i, c in enumerate(end):
            if c != 'X':
                b.append((c, i))
        if len(a) != len(b):
            return False
        
        for (x, i), (y, j) in zip(a, b):
            if x != y:
                return False
            if x == 'L' and i < j:
                return False
            if x == 'R' and i > j:
                return False
        return True
