class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:     
        @cache
        def dp(candidate: tuple[int], remainingTotal: int) -> bool:
            if candidate[-1] >= remainingTotal:
                return True
            for i in range(len(candidate)):
                if not dp(candidate[:i] + candidate[i + 1:], remainingTotal - candidate[i]):
                    return True
            return False
        
        candidate = tuple(range(1, maxChoosableInteger + 1))
        if sum(candidate) < desiredTotal:
            return False
        return dp(candidate, desiredTotal)
           