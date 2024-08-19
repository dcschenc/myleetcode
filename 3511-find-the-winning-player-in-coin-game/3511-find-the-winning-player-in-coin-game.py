class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        cnt = 0
        while x > 0 and y >= 4:
            x -= 1
            y -= 4
            cnt += 1
            
        return 'Alice' if cnt % 2 == 1 else 'Bob'
