class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # n = len(board)
        # target = n * n

        def get_coordinates(square):
            r, c = divmod(square - 1, n)
            # Check if the row is in normal order
            if r % 2 == 0:  
                return n - 1 - r, c
            else:  # Reverse the column if the row is in reverse order
                return n - 1 - r, n - 1 - c

        # visited = set()
        # queue = deque([(1, 0)])  # (current_square, moves)
        
        # while queue:
        #     curr_square, moves = queue.popleft()

        #     if curr_square == target:
        #         return moves

        #     if curr_square in visited:
        #         continue
        #     visited.add(curr_square)

        #     for i in range(curr_square + 1, min(curr_square + 7, target + 1)):
        #         r, c = get_coordinates(i)
        #         if board[r][c] != -1:
        #             next_square = board[r][c]
        #         else:
        #             next_square = i
        #         queue.append((next_square, moves + 1))

        # return -1

        n, queue = len(board), deque()
        queue.append(1)
        visited = set()
        steps = 0
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == n * n:
                    return steps
                if cur in visited:
                    continue
                visited.add(cur)                
               
                for nb in range(cur + 1, min(cur + 6, n * n) + 1):    
                    x, y = get_coordinates(nb)   
                    if board[x][y] != -1:
                        queue.append(board[x][y])   
                    else:          
                        queue.append(nb)
                      
            steps += 1
        return -1