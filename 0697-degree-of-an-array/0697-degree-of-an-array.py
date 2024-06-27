from collections import Counter
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:       
        cnt = Counter(nums)
        degree = cnt.most_common()[0][1]
        left, right = {}, {}
        for i, v in enumerate(nums):
            if v not in left:
                left[v] = i
            right[v] = i
            
        ans = inf
        for v in nums:
            if cnt[v] == degree:
                t = right[v] - left[v] + 1
                if ans > t:
                    ans = t
        return ans

        # hm = {}
        # degree = 0
        # ### hm [0]: start, [1]: end, [2] degree
        # for i, num in enumerate(nums):
        #     if num not in hm:
        #         hm[num] = [i, i, 1]
        #         if degree < 1:
        #             degree = 1
        #     else:
        #         hm[num][1] = i
        #         hm[num][2] += 1
        #         if hm[num][2] > degree:
        #             degree = hm[num][2]
        # min_l = 500001
        # for k, v in hm.items():
        #     i, j, cnt = v
        #     if cnt == degree:
        #         if j == -1:
        #             j = 0
        #         if j - i + 1 < min_l:
        #             min_l = j-i+1
        # return min_l

