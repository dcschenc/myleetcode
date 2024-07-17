class Solution:
    # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1475.Final%20Prices%20With%20a%20Special%20Discount%20in%20a%20Shop
    def finalPrices(self, prices: List[int]) -> List[int]:
        stk = []   # to record the index
        ans = prices[:]
        for i, v in enumerate(prices):
            while stk and prices[stk[-1]] >= v:
                ans[stk.pop()] -= v
            stk.append(i)
        return ans

        # n = len(prices)
        # ans = []
        # for i in range(n):
        #     ans.append(prices[i])
        #     for j in range(i+1, n):
        #         if prices[j] <= prices[i]:
        #             ans[-1] -= prices[j]
        #             break
        # return ans
