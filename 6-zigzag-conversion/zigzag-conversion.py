class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        # Create a list of empty strings to represent each row
        rows = [''] * numRows
        index, step = 0, 1

        for char in s:
            rows[index] += char
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1
            index += step

        # Concatenate the rows to form the final zigzag conversion
        result = ''.join(rows)
        return result

        if numRows == 1:
            return s

        n = len(s)
        i = 0
        cur = []
        res = []
        cur = 0
        j = 0
        mat = [[0] * (n) for i in range(numRows)]
        while cur < n:         
            mat[i][j] = s[cur]
            i += 1
            cur += 1
            if i == numRows:
                j += 1
                i -= 2
                while i > 0 and cur < n:
                    mat[i][j] = s[cur]
                    cur += 1
                    j += 1
                    i -= 1
        col = j
        res = ''
        for i in range(numRows):
            for j in range(col+1):
                if mat[i][j] != 0:
                    res += mat[i][j]
        return res