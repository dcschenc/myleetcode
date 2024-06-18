class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # j = 0

        # for i in range(len(nums)):
        #     if nums[i] == val:
        #         nums[i] = None
        #     else:
        #         if nums[j] == None:
        #             nums[j], nums[i] = nums[i], nums[j]
        
        #         j += 1

        # return j
        # i = 0
        # k = 0
        # while i < len(nums):
        #     if nums[i] == val:
        #         j = i+1
        #         while j < len(nums):
        #             nums[j-1] = nums[j]                    
        #             j += 1
        #         k +=1
        #     else:
        #         i += 1
        #     if i + k == len(nums):
        #         break
        # # print(k)
        # return len(nums) - k 

        l = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
        return l