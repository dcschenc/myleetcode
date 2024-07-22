class Solution:
    # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1658.Minimum%20Operations%20to%20Reduce%20X%20to%20Zero
    def minOperations(self, nums: List[int], x: int) -> int:
        total_sum = sum(nums)
        target_sum = total_sum - x
        n = len(nums)

        if target_sum < 0:
            return -1
        if target_sum == 0:
            return n

        max_len = -1
        current_sum = 0
        left = 0

        for right in range(n):
            current_sum += nums[right]

            while current_sum > target_sum and left <= right:
                current_sum -= nums[left]
                left += 1

            if current_sum == target_sum:
                max_len = max(max_len, right - left + 1)

        return n - max_len if max_len != -1 else -1


        x = sum(nums) - x
        seen = {0: -1}
        ans = inf
        s, n = 0, len(nums)
        for i, v in enumerate(nums):
            s += v
            if s - x in seen:
                j = seen[s - x]
                ans = min(ans, n - (i - j))
            if s not in seen:
                seen[s] = i
        return -1 if ans == inf else ans

        # left, right = 0, len(nums) - 1
        # cnt = 0
        # while left <= right:
        #     if x < nums[left] and x < nums[right]:
        #         return -1
        #     elif x == nums[left] or x == nums[right]:
        #         return cnt + 1
        #     elif x > nums[left] and x < nums[right]:
        #         x -= nums[left]
        #         left += 1
        #     elif x < nums[left] and x > nums[right]:
        #         x -= nums[right]
        #         right -= 1
        #     else:
        #         if nums[left] > nums[right]:
        #             x -= nums[left]
        #             left += 1
        #         else:
        #             x -= nums[right]
        #             right -= 1
        #     cnt += 1
        # print(cnt)
        # return cnt if x == 0 else -1
        