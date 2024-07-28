class Solution:
    def widestPairOfIndices(self, nums1: List[int], nums2: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1983.Widest%20Pair%20of%20Indices%20With%20Equal%20Range%20Sum
        d = {0: -1}
        ans = s = 0
        for i, (a, b) in enumerate(zip(nums1, nums2)):
            s += a - b
            if s in d:
                ans = max(ans, i - d[s])
            else:
                d[s] = i
        return ans

        # n = len(nums1)
        # if n == 1 and nums1[0] == nums2[0]: return 1
        # presum1, presum2 = [0] * (n + 1), [0] * (n + 1)
        # for i in range(n+1):
        #     # presum1[i] = nums1[i]
        #     # presum2[i] = nums2[i]
        #     # if i > 0:
        #         presum1[i] += presum1[i-1] + nums1[i-1]
        #         presum2[i] += presum2[i-1] + nums2[i-1]
        # print(presum1, presum2)
        # dist = 0
        # for i in range(n+1):
        #     for j in range(i+1, n+1):
        #         if presum1[j] - presum1[i] == presum2[j] - presum2[i]:
        #             dist = max(dist, j - i )
        # return dist