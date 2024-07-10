class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        weight.sort()
        total_sum = 0
        cnt = 0
        for i in range(len(weight)):
            if total_sum + weight[i] > 5000:
                break
            total_sum += weight[i]
            cnt += 1
        return cnt