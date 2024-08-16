class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        ans = 0
        happiness.sort(reverse=True)
        cnt = 0
        while k > 0:
            ans += max(happiness[cnt] - cnt, 0)
            cnt += 1
            k -= 1
        return ans