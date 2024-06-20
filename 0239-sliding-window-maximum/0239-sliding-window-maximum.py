class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
    
        result = []
        queue = deque()

        for i in range(len(nums)):
            # Remove elements that are outside the window
            if queue and queue[0] < i - k + 1:
                queue.popleft()
            
            # Remove elements that are smaller than the current element
            while queue and nums[i] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(i)

            # Add the maximum element for the current window to the result
            if i >= k - 1:
                result.append(nums[queue[0]])

        return result
        
        # curMax = max(nums[:k])
        # res = [curMax]
        # for R in range(k, len(nums)):   
        #     if curMax < nums[R]:
        #         curMax = nums[R]
        #     else:
        #         if nums[R-k] == curMax:
        #             curMax = max(nums[R-k+1:R+1])
        #     res.append(curMax)
        # return res