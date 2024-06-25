class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0500-0599/0539.Minimum%20Time%20Difference
        if len(timePoints) > 1440: return 0
        
        nums = sorted(int(x[:2]) * 60 + int(x[3:]) for x in timePoints)
        nums.append(nums[0] + 1440)
        return min(b - a for a, b in pairwise(nums))

        # res = []
        # for t in timePoints:
        #     res.append(int(t[:2])*60 + int(t[3:]))
        # res.sort()
        # # print(res)
        # min_m = 24*60 + 1        
        # for i, t in enumerate(res):
        #     if i > 0:
        #         diff_1 = abs(res[i] - res[i-1])
        #         diff_2 = 1440 - res[i] + res[0]
        #         # print(diff_1, diff_2, min_m)
        #         min_m = min(min_m, diff_1, diff_2)
       
        return min_m