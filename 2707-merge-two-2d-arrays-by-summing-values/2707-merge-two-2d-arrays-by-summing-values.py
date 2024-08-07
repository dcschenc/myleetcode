class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2570.Merge%20Two%202D%20Arrays%20by%20Summing%20Values
        cnt = Counter()
        for i, v in nums1 + nums2:
            cnt[i] += v
        return sorted(cnt.items())

        # m, n = len(nums1), len(nums2)
        # i, j = 0, 0
        # ans = []
        # while i < m and j < n:
        #     if nums1[i][0] == nums2[j][0]:
        #         ans.append([nums1[i][0], nums1[i][1] + nums2[j][1]])
        #         i += 1
        #         j += 1
        #     elif nums1[i][0] < nums2[j][0]:
        #         ans.append([nums1[i][0], nums1[i][1]])
        #         i += 1
        #     else:
        #         ans.append([nums2[j][0], nums2[j][1]])
        #         j += 1

        # while i < m:
        #     ans.append([nums1[i][0], nums1[i][1]])
        #     i += 1
        # while j < n:
        #     ans.append([nums2[j][0], nums2[j][1]])
        #     j += 1            
        # return ans