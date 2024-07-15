class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1406.Stone%20Game%20III
        @cache
        def dfs(i: int) -> int:
            if i >= n:
                return 0
            ans, s = -inf, 0
            for j in range(3):
                if i + j >= n:
                    break
                s += stoneValue[i + j]
                ans = max(ans, s - dfs(i + j + 1))
            return ans

        n = len(stoneValue)
        ans = dfs(0)
        if ans == 0:
            return 'Tie'
        return 'Alice' if ans > 0 else 'Bob'

        
        @cache
        def dp(i):
            if i >= n:
                return 0
            ans = stoneValue[i] - dp(i+1)
            if i + 1 < n:
                ans = max(ans, stoneValue[i] + stoneValue[i+1] - dp(i + 2))
            if i + 2 < n:
                ans = max(ans, stoneValue[i] + stoneValue[i+1] + stoneValue[i+2] - dp(i + 3))

            return ans                 

        
        n = len(stoneValue)
        alice = dp(0)
        if alice == 0:
            return 'Tie'
        elif alice > 0:
            return 'Alice'
        else:
            return 'Bob'