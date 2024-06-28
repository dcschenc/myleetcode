class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0870.Advantage%20Shuffle

        nums1.sort()
        t2 = sorted((v, i) for i, v in enumerate(nums2))
        n = len(nums1)
        ans = [0] * n
        i, j = 0, n - 1
        for num in nums1:
            if num <= t2[i][0]:
                ans[t2[j][1]] = num
                j -= 1
            else:
                ans[t2[i][1]] = num
                i += 1
        return ans