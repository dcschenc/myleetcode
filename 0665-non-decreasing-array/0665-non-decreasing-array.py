class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/0600-0699/0665.Non-decreasing%20Array
        def is_sorted(nums: List[int]) -> bool:
            return all(a <= b for a, b in pairwise(nums))

        n = len(nums)
        for i in range(n - 1):
            a, b = nums[i], nums[i + 1]
            if a > b:
                nums[i] = b
                if is_sorted(nums):
                    return True
                nums[i] = nums[i + 1] = a
                return is_sorted(nums)
        return True
        
        # cnt = 0
        # for i in range(1, len(nums)):           
        #     if nums[i] < nums[i-1]:
        #         cnt += 1
        #         if cnt > 1:
        #             return False
        #         if i - 2 < 0 or nums[i - 2] <= nums[i]:
        #             nums[i - 1] = nums[i]
        #         else:
        #             nums[i] = nums[i - 1]
            
        # return True

# whenever we find a decreasing pair (nums[i] < nums[i - 1]), we try to modify the array to make it non-decreasing. 
# If we can't modify it in a way that satisfies the condition, we return False. Otherwise, we continue checking.