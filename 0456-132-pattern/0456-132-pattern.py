class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/0400-0499/0456.132%20Pattern
        if len(nums) < 3:
            return False
        
        stack = []
        second = float('-inf')
        
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < second:
                return True
            while stack and stack[-1] < nums[i]:
                second = stack.pop()
            stack.append(nums[i])
        
        return False
        
        n = len(nums)
        if n < 3: return False
        stack = []
        third = float('-inf')  
        for i in range(n - 1, -1, -1):
            if nums[i] < third:  return True
            while stack and nums[i] > stack[-1]:
                third = stack.pop()
            stack.append(nums[i])

        return False  

