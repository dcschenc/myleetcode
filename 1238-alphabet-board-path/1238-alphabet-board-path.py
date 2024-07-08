from collections import Counter
class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/1100-1199/1138.Alphabet%20Board%20Path
        i = j = 0
        ans = []
        for c in target:
            v = ord(c) - ord("a")
            x, y = v // 5, v % 5
            while j > y:
                j -= 1
                ans.append("L")
            while i > x:
                i -= 1
                ans.append("U")
            while j < y:
                j += 1
                ans.append("R")
            while i < x:
                i += 1
                ans.append("D")
            ans.append("!")
        return "".join(ans)


        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        matrix = [['0'] * 5 for i in range(6)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                matrix[i][j] = board[i][j]
        cur = (0, 0)
        result = ''
        for c in target:
            queue = deque()
            visited = []
            queue.append((cur[0], cur[1], ''))
            while queue:                
                for _ in range(len(queue)):                   
                    x, y, path = queue.popleft()
                    if matrix[x][y] == c:
                        path += '!'
                        cur = (x, y)
                        break
                    if (x, y) in visited:
                        continue
                    visited.append((x, y))
                    if x + 1 <= 4 or x + 1 == 5 and y == 0:                        
                        queue.append((x+1, y, path + 'D')) 
                    if x - 1 >= 0:                       
                        queue.append((x-1, y, path + 'U'))
                    if y + 1 <= 4 and x != 5:                        
                        queue.append((x, y+1, path + 'R'))
                    if y - 1 >= 0:                        
                        queue.append((x, y-1, path + 'L'))
                
                if len(path) > 0 and path[-1] == '!':
                    result += path
                    break
        return result

        # board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        # hm = {}
        # for i in range(len(board)):
        #     for j in range(len(board[i])):
        #         hm[board[i][j]] = (i, j)
        # cur = (0, 0)
        # path = ''
        # for c in target:
        #     i, j = cur
        #     x, y = hm[c]              
        #     if c == 'z':
        #         if j == 0:
        #             path = path +  'D' * (x - i)                    
        #         else:
        #             path += 'D' * (4 - i)
        #             path += 'L' * j + 'D'
        #     else:
        #         if x < i:
        #             while x != i:
        #                 i -= 1
        #                 path += 'U'
        #         elif x > i:
        #             while x != i:
        #                 i += 1
        #                 path += 'D'

        #         if y < j:
        #             while y != j:
        #                 j -= 1
        #                 path += 'L'
        #         elif y > j:
        #             while y != j:
        #                 j += 1
        #                 path += 'R'
                
        #     path += '!'
        #     cur = (x, y)
        # return path