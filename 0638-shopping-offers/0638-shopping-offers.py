class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:              

        def dfs(prices, specials, needs):
            if tuple(needs) in memo: return memo[tuple(needs)]            
            '''
            return minimum success path, choosing between the price or special
            '''
            cost = sum(prices[i] * needs[i] for i in range(len(prices)))
            for offer in specials:
                # consider the special offer
                updated_needs = [needs[j] - offer[j] for j in range(len(needs))]

                if all(updated_needs[j] >= 0 for j in range(len(needs))):
                    # total cost or pay for the special
                    cost = min(cost, offer[-1] + dfs(prices, specials, updated_needs))

            memo[tuple(needs)] = cost
            return cost

        memo = {}
        return dfs(price, special, needs)

        # # https://github.com/doocs/leetcode/tree/main/solution/0600-0699/0638.Shopping%20Offers
        # d = {}
        # def dfs(price, special, needs):
        #     if not needs: return 0
        #     # calculate the price without special offer
        #     res = sum([price[i] * needs[i] for i in range(len(needs))])
        #     # try to use each special offer
        #     for offer in special:
        #         # check if we can use this offer
        #         for i in range(len(needs)):
        #             if needs[i] < offer[i]:
        #                 break
        #         else:
        #             # use this offer
        #             tmp = [needs[j] - offer[j] for j in range(len(needs))]
        #             if tuple(tmp) not in d:
        #                 d[tuple(tmp)] = dfs(price, special, tmp)
        #             res = min(res, offer[-1] + d[tuple(tmp)])
        #     return res

        # return dfs(price, special, needs)