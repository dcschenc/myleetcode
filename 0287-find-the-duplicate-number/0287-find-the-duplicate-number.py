class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # 'low' and 'high' represent the range of values of the target
        low = 1
        high = len(nums) - 1        
        while low <= high:
            cur = (low + high) // 2
            # Count how many numbers are less than or equal to 'cur'
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1
                
        return duplicate

        # left, right = 1, len(nums)
        # while left < right:
        #     mid = (left+right)//2
        #     cnt = 0
        #     for val in nums:
        #         if val <=mid:
        #             cnt += 1
        #     if cnt <= mid:
        #         left = mid + 1
        #     else:
        #         right = mid
        # return right
            
        # Floyd's Tortoise and Hare Algorithm
        # Initialize the pointers.
        tortoise = nums[0]
        hare = nums[0]

        # Phase 1: Move hare and tortoise to meet inside the cycle.
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        # Phase 2: Find the entrance to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]

        return tortoise