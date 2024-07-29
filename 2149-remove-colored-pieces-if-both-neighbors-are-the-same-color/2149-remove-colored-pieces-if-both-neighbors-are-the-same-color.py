class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2038.Remove%20Colored%20Pieces%20if%20Both%20Neighbors%20are%20the%20Same%20Color
        alice = 0
        bob = 0
        for i in range(1, len(colors) - 1):
            if colors[i - 1] == colors[i] == colors[i + 1]:
                if colors[i] == "A":
                    alice += 1
                else:
                    bob += 1
        
        return alice - bob >= 1
        
        # moves_A, moves_B = 0, 0
        # n = len(colors)
        # prev = 0
        # for i in range(1, n+1):
        #     if i == n or colors[i] != colors[prev]:
        #         if i - prev >= 3:
        #             if colors[prev] == 'A':
        #                 moves_A += (i - prev) - 2
        #             else:
        #                 moves_B += (i - prev) - 2
        #         prev = i
        # return moves_A - 1 >= moves_B
           