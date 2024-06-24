class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        # start from i and remove continues ball
        def remove_same(s, i):
            if i < 0: return s            
            left = right = i
            while left > 0 and s[left-1] == s[i]:
                left -= 1
            while right+1 < len(s) and s[right+1] == s[i]:
                right += 1            
            length = right - left + 1
            if length >= 3:
                new_s = s[:left] + s[right+1:]
                return remove_same(new_s, left-1)
            else:
                return s

        hand = "".join(sorted(hand))
        # board, hand and step
        q = collections.deque([(board, hand, 0)])
        visited = set([(board, hand)])
        while q:
            cur_board, cur_hand, step = q.popleft()
            for i in range(len(cur_board) + 1):
                for j in range(len(cur_hand)):
                    # skip the continue balls in hand  --- pruning
                    if j > 0 and cur_hand[j] == cur_hand[j-1]:
                        continue                    
                    # only insert at the begin of continue balls in board
                    if i > 0 and cur_board[i-1] == cur_hand[j]: # left side same color
                        continue
                    
                    pick = False
                    # 1. same color with right
                    # 2. left and right are same but pick is different
                    if i < len(cur_board) and cur_board[i] == cur_hand[j]:
                        pick = True
                    if 0 < i < len(cur_board) and cur_board[i-1] == cur_board[i] and cur_board[i] != cur_hand[j]:
                        pick = True                    
                    if pick:
                        new_board = remove_same(cur_board[:i] + cur_hand[j] + cur_board[i:], i)
                        new_hand = cur_hand[:j] + cur_hand[j+1:]
                        if not new_board:
                            return step + 1
                        if (new_board, new_hand) not in visited:
                            q.append((new_board, new_hand, step + 1))
                            visited.add((new_board, new_hand))
        return -1