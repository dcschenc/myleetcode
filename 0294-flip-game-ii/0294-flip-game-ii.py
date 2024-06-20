class Solution:
    def canWin(self, currentState: str) -> bool:   
        def dfs(s):
            if s in memo:
                return memo[s]
            for i in range(len(s) - 1):
                if s[i:i + 2] == "++":
                    opponentMove = s[:i] + "--" + s[i + 2:]
                    if not dfs(opponentMove):
                        memo[s] = True
                        return True

            memo[s] = False
            return False
        s = currentState
        memo = {}
        return dfs(s)