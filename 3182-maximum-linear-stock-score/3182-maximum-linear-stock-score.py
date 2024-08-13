class Solution:
    def maxScore(self, prices: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2898.Maximum%20Linear%20Stock%20Score
        hm = defaultdict(int)
        for i, p in enumerate(prices):
            hm[p - i] += p
        return max(hm.values())