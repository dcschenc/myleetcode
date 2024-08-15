class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2934.Minimum%20Operations%20to%20Maximize%20Last%20Elements%20in%20Arrays
        def f(x: int, y: int) -> int:
            cnt = 0
            for a, b in zip(nums1[:-1], nums2[:-1]):
                if a <= x and b <= y:
                    continue
                if not (a <= y and b <= x):
                    return -1
                cnt += 1
            return cnt

        a, b = f(nums1[-1], nums2[-1]), f(nums2[-1], nums1[-1])
        return -1 if a + b == -2 else min(a, b + 1)