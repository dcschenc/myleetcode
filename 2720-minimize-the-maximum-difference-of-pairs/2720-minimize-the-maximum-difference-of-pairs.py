class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:     
        # https://github.com/doocs/leetcode/tree/main/solution/2600-2699/2616.Minimize%20the%20Maximum%20Difference%20of%20Pairs
        def check(diff: int) -> bool:
            cnt = i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= diff:
                    cnt += 1
                    i += 2
                else:
                    i += 1
            return cnt >= p

        nums.sort()
        return bisect_left(range(nums[-1] - nums[0] + 1), True, key=check)


        # Find the number of valid pairs by greedy approach
        def countValidPairs(threshold):
            index, count = 0, 0
            while index < n - 1:
                # If a valid pair is found, skip both numbers.
                if nums[index + 1] - nums[index] <= threshold:
                    count += 1
                    index += 1
                index += 1
            return count
        
        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = left + (right - left) // 2
            # If there are enough pairs, look for a smaller threshold.
            # Otherwise, look for a larger threshold.
            if countValidPairs(mid) >= p:
                right = mid
            else:
                left = mid + 1
        return left  