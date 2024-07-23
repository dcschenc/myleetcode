class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:   
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1695.Maximum%20Erasure%20Value
        left, right = 0, 0
        window_sum = 0
        max_erasure_value = 0
        current_set = set()

        while right < len(nums):
            if nums[right] not in current_set:
                current_set.add(nums[right])
                window_sum += nums[right]
                max_erasure_value = max(max_erasure_value, window_sum)
                right += 1
            else:
                while nums[left] != nums[right]:
                    current_set.remove(nums[left])
                    window_sum -= nums[left]
                    left += 1
                current_set.remove(nums[left])
                window_sum -= nums[left]
                left += 1

        return max_erasure_value