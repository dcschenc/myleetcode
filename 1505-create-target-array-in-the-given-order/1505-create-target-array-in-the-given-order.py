class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        target = []
        for num, i in zip(nums, index):
            target.insert(i, num)
        return target
        
        # ans = []
        # for i, idx in enumerate(index):
        #     num = nums[i]
        #     if idx > len(ans) - 1:
        #         ans.append(num)
        #     else:
        #         ans.append(-1)                
        #         j = len(ans) - 1
        #         while j > idx:
        #             ans[j] = ans[j-1]
        #             j -= 1                
        #         ans[j] = num
        # return ans