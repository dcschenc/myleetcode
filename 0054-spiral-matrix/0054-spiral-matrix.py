class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows, columns = len(matrix), len(matrix[0])
        up = left = 0
        right = columns - 1
        down = rows - 1

        while len(result) < rows * columns:
            # Traverse from left to right.
            for col in range(left, right + 1):
                result.append(matrix[up][col])

            # Traverse downwards.
            for row in range(up + 1, down + 1):
                result.append(matrix[row][right])

            # Make sure we are now on a different row.
            if up != down:
                # Traverse from right to left.
                for col in range(right - 1, left - 1, -1):
                    result.append(matrix[down][col])

            # Make sure we are now on a different column.
            if left != right:
                # Traverse upwards.
                for row in range(down - 1, up, -1):
                    result.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return result

        m,n = len(matrix), len(matrix[0])
        res = []
        if n == 1:
            for i in range(m):
                res.append(matrix[i][0])
        else:
            
            for i in range(math.ceil(m/2)):
                if (i + 1)*2 - 1 > n:
                    break
                # 1st row
                for j in range(i, n-i):
                    res = res + [matrix[i][j]]   
                # 1st column 
                if i == m//2:
                    continue
                for k in range(i+1,m-i):
                    res = res + [matrix[k][j]]
                for p in range(j-1,i,-1):
                    res = res + [matrix[k][p]]
                if j-1 < i:
                    continue             
                for q in range(k,i,-1):
                    res = res + [matrix[q][i]]
                # print(res)   
        
        # print(res)
        return res