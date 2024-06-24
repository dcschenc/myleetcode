class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_len = 0
        count = 0
        for n in nums:
            if n == 1:
                count += 1
            else:
                max_len = max(max_len, count)
                count = 0
        return max(max_len, count)
        
        # start = -1
        # for i,val in enumerate(nums):
        #     if val != 1:                
        #         start = -1
        #     else:
        #         if start == -1:
        #             start = i
        #         if i - start + 1 > max_len:                    
        #             max_len = i - start + 1
        # return max_len
                