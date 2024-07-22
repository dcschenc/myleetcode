class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        m = len(accounts)
        max_sum = 0
        for i in range(m):
            # current_sum = sum(accounts[i])
            # if current_sum > max_sum:
            #     max_sum = sum(accounts[i])
            max_sum = max(max_sum, sum(accounts[i]))
        return max_sum