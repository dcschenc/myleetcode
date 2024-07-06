class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n, ans = len(values), 0
        max_prev = 0
        for i in range(n):
            ans = max(ans, values[i] - i + max_prev)
            max_prev = max(max_prev, values[i] + i)
        return ans
        
        # n = len(values)
        # ans = -float('inf')
        # for i in range(n):
        #     cur_max, cur_val = -float('inf'), -1
        #     for j in range(i + 1, n):
        #         if j > i + 1 and cur_val != -1 and values[j] <= cur_val:
        #             continue
        #         cur = values[i] + values[j] + i - j
        #         if cur > cur_max:
        #             cur_max = cur
        #             cur_val = values[j] 
        #     ans = max(ans, cur_max)
        # return ans