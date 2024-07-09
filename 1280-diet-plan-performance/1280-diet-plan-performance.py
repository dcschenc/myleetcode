from itertools import accumulate
class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        presum = list(accumulate(calories, initial=0))
        # print(presum)
        ans = 0
        for i in range(k, len(calories) + 1):
            cal = presum[i] - presum[i-k]
            if cal < lower:
                ans -= 1
            elif cal > upper:
                ans += 1
        return ans

        # presum = sum(calories[:k-1])
        # points = 0
        # for i in range(k-1, len(calories)):
        #     presum += calories[i]
        #     if presum < lower:
        #         points -= 1
        #     elif presum > upper:
        #         points += 1
        #     presum -= calories[i-k+1]
        # return points