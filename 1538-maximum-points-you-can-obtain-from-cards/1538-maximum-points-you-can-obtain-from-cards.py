class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1423.Maximum%20Points%20You%20Can%20Obtain%20from%20Cards
        ans = cur = sum(cardPoints[-k:])
        for i in range(k):
            cur = cur + cardPoints[i] - cardPoints[-k+i]
            ans = max(ans, cur)
        return ans

        # n = len(cardPoints)
        # if k == n:
        #     return sum(cardPoints)
        # m = n - k 
        # cur = sum(cardPoints[:m])
        # min_sum = cur
        # for i in range(m, n):
        #     cur = cur - cardPoints[i-m] + cardPoints[i]     
        #     min_sum = min(min_sum, cur)
        # return sum(cardPoints) - min_sum