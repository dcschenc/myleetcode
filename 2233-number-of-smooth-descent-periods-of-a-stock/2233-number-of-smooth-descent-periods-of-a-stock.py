class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        # ans = 0
        # cur = 1
        # n = len(prices)
        # for i in range(1, n):
        #     if prices[i] + 1 == prices[i-1]:
        #         cur += 1
        #         if i == n-1:
        #             ans += cur * (cur + 1)//2
        #     else:               
        #         ans += cur * (cur + 1)//2
        #         cur = 1
        # if cur == 1:
        #     ans += 1
        # return ans
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2110.Number%20of%20Smooth%20Descent%20Periods%20of%20a%20Stock
        ans = 0
        i, n = 0, len(prices)
        while i < n:
            j = i + 1
            while j < n and prices[j - 1] - prices[j] == 1:
                j += 1
            cnt = j - i
            ans += (1 + cnt) * cnt // 2
            i = j
        return ans