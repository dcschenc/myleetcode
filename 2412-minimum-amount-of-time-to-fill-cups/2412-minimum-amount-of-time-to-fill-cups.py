class Solution:
    def fillCups(self, amount: List[int]) -> int:
        ans = 0
        while sum(amount):
            amount.sort()
            ans += 1
            amount[2] -= 1
            amount[1] = max(0, amount[1] - 1)
        return ans
        
        # ans = 0
        # amount = [v for v in amount if v > 0]
        # amount.sort()
        # while len(amount) > 0:
        #     amount[-1] -= 1
        #     if len(amount) > 1:
        #         amount[-2] -= 1    
        #     amount = [v for v in amount if v > 0]        
        #     amount.sort()
        #     ans += 1
        # return ans