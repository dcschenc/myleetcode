class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        n = len(nums)
        for i in range(n - 2):
            left, right = i + 1, n - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum < target:                    
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count
        
        nums.sort()
        cnt = 0
        for i in range(len(nums)):            
            if nums[i] >= target and nums[i] > 0:
                break          
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] >= target and nums[j] > 0:
                    break
                for k in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[k] >= target:
                        break
                    cnt += 1
        return cnt
               