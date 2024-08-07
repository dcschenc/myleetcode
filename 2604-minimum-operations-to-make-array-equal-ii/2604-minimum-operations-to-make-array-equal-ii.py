class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2541.Minimum%20Operations%20to%20Make%20Array%20Equal%20II
        ans = x = 0
        for a, b in zip(nums1, nums2):
            if k == 0:
                if a != b:
                    return -1
                continue
            if (a - b) % k:
                return -1
            y = (a - b) // k
            ans += abs(y)
            x += y
        return -1 if x else ans // 2

        # ans, n = 0, len(nums1)
        # add, substract = 0, 0
        # for i in range(n):
        #     if k == 0:
        #         if nums1[i] != nums2[i]:
        #             return -1
        #         continue

        #     if nums1[i] > nums2[i]:
        #         if (nums1[i] - nums2[i]) % k != 0:
        #             return -1
        #         else:
        #             add += (nums1[i] - nums2[i]) // k                    
        #     elif nums1[i] < nums2[i]:
        #         if (nums2[i] - nums1[i]) % k != 0:
        #             return -1
        #         else:
        #             substract += (nums2[i] - nums1[i]) // k

        # return add if add == substract else -1

            