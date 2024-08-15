class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        n = primeOne * primeTwo
        dp = [False for _ in range(n)]
        dp[0] = True
        
        for i in range(1, n):
            if i - primeOne >= 0:
                dp[i] = dp[i] | dp[i - primeOne]
            if i - primeTwo >= 0:
                dp[i] = dp[i] | dp[i - primeTwo]
                
        for i in range(n-1, -1, -1):
            if dp[i] is False:
                return i