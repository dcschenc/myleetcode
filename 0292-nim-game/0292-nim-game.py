class Solution:
    def canWinNim(self, n: int) -> bool:        
        if n%4 == 0:
            return False
        return True

        # if not self.canWinNim(n-1) or not self.canWinNim(n-2) or not self.canWinNim(n-3):
        #     return True
        # else:
        #     return False