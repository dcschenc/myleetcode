class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def f(arr: List[int]) -> int:
            s = 0
            for i, x in enumerate(arr):
                k = 2 if (i and arr[i - 1] == 10) or (i > 1 and arr[i - 2] == 10) else 1
                s += k * x
            return s

        a, b = f(player1), f(player2)
        return 1 if a > b else (2 if b > a else 0)

        # score1, score2 = 0, 0
        # for i in range(len(player1)):
        #     c = 2 if i >= 2 and 10 in player1[i-2:i] or i >= 1 and player1[i-1] == 10 else 1               
        #     score1 += player1[i] * c
        #     c = 2 if i >= 2 and 10 in player2[i-2:i] or i >= 1 and player2[i-1] == 10 else 1               
        #     score2 += player2[i] * c
      
        # if score1 == score2:
        #     return 0
        # elif score1 > score2:
        #     return 1
        # else:
        #     return 2
        