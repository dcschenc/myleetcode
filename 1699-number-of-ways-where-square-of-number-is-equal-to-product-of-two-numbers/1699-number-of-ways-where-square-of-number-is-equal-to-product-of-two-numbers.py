class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        def count(target, nums):         
            seen = defaultdict(int)
            total = 0
            for j in range(len(nums)):
                val = target // nums[j] 
                if target % nums[j] == 0 and val in seen:
                    total += seen[target // nums[j]]
                seen[nums[j]] += 1
            return total

        total = 0
        m, n = len(nums1), len(nums2)
        for i in range(m):
            target = nums1[i] ** 2
            total += count(target, nums2)
        for i in range(n):
            target = nums2[i] ** 2
            total += count(target, nums1)
        return total

        # for i in range(m):
        #     target = nums1[i] ** 2
        #     seen = defaultdict(int)
        #     for j in range(n):
        #         val = target // nums2[j] 
        #         if target % nums2[j] == 0 and val in seen:
        #             total += seen[target // nums2[j]]
        #         seen[nums2[j]] += 1

        # for i in range(n):
        #     target = nums2[i] ** 2
        #     seen = defaultdict(int)
        #     for j in range(m):
        #         val = target // nums1[j] 
        #         if target % nums1[j] == 0 and val in seen:
        #             total += seen[target // nums1[j]]
        #         seen[nums1[j]] += 1
        # return total