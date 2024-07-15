class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        # Generate all Fibonacci numbers less than or equal to k
        fibs = [1, 1]
        while fibs[-1] < k:
            fibs.append(fibs[-1] + fibs[-2])
        
        # Initialize the number of Fibonacci numbers used
        count = 0
        
        # Iterate from the largest Fibonacci number
        for i in range(len(fibs) - 1, -1, -1):
            while k >= fibs[i]:
                k -= fibs[i]
                count += 1
                if k == 0:
                    break
            if k == 0:
                break
        
        return count


        # dp = []
        # dp.append(1)
        # dp.append(1)
        # while dp[-1] + dp[-2] <= k:            
        #     dp.append(dp[-1] + dp[-2])

        # ans = 0
        # while dp:
        #     if k == dp[-1]:
        #         return ans + 1
        #     if k > dp[-1]:
        #         ans += 1
        #         k = k - dp[-1]
        #     dp = dp[:-1]
            
        # return ans
