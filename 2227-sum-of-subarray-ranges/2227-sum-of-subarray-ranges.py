class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2100-2199/2104.Sum%20of%20Subarray%20Ranges
        # Monotonic Stack
        # https://leetcode.com/problems/sum-of-subarray-ranges/editorial/
        n, answer = len(nums), 0 
        stack = []
        
        # Find the sum of all the minimum.
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer -= nums[mid] * (mid - left) * (right - mid)
            stack.append(right)

        # Find the sum of all the maximum.
        stack.clear()
        for right in range(n + 1):
            while stack and (right == n or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                answer += nums[mid] * (mid - left) * (right - mid)
            stack.append(right)
        
        return answer

        # n, answer = len(nums), 0 
        # stack = []        
        # # Find the sum of all the minimum.
        # for right in range(n + 1):
        #     while stack and (right == n or nums[stack[-1]] >= nums[right]):
        #         mid = stack.pop()
        #         left = -1 if not stack else stack[-1]
        #         answer -= nums[mid] * (mid - left) * (right - mid)
        #     stack.append(right)

        # # Find the sum of all the maximum.
        # stack.clear()
        # for right in range(n + 1):
        #     while stack and (right == n or nums[stack[-1]] <= nums[right]):
        #         mid = stack.pop()
        #         left = -1 if not stack else stack[-1]
        #         answer += nums[mid] * (mid - left) * (right - mid)
        #     stack.append(right)
        
        # return answer

        n = len(nums)
        ans = 0
        for i in range(n):
            min_v = max_v = nums[i]
            for j in range(i+1, n):
                min_v = min(min_v, nums[j])
                max_v = max(max_v, nums[j])
                ans += max_v - min_v
        return ans