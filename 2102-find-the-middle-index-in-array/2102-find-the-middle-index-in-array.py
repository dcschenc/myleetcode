class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1991.Find%20the%20Middle%20Index%20in%20Array
        left, right = 0, sum(nums)
        for i, x in enumerate(nums):
            right -= x
            if left == right:
                return i
            left += x
        return -1

        n = len(nums)

        presum = [0] * (n + 1)
        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + nums[i-1]
        postsum = 0
        ans = -1
        for i in range(n, 0, -1):
            if presum[i-1] == postsum:
                ans = i - 1
            postsum += nums[i-1]
        return ans

        # left, right = 0, sum(nums)
        # for i, x in enumerate(nums):
        #     right -= x
        #     if left == right:
        #         return i
        #     left += x
        # return -1