class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # nums1.sort()
        # nums2.sort()
        # nums3.sort()
        # nums4.sort()
        n, hm, res = len(nums1), defaultdict(int), 0
        for i in range(n):
            for j in range(n):
                hm[nums1[i] + nums2[j]] += 1 

        for k in range(n):
            for l in range(n):
                res += hm[0 - (nums3[k] + nums4[l])]

        return res

        # n = len(nums1)
        # dict_ = defaultdict(int)
        # count = 0
        # for i in range(n):
        #     for j in range(n):
        #         key = nums1[i] + nums2[j]
        #         dict_[key] += 1

        # for k in range(n):
        #     for p in range(n):
        #         key = nums3[k] + nums4[p]
        #         count += dict_[0-key]
        # return count
                    