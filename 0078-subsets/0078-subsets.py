class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ########## O(2^N) ########
        # def backtrack(nums, curr):
        #     res.append(curr)
        #     for i, v in enumerate(nums):
        #         backtrack(nums[i+1:], curr+[v])
        
        # res = []
        # backtrack(nums, [])
        # return res
        
        def backtrack(start, path):
            result.append(path[:])
            if start == n: 
                return            
            for i in range(start, len(nums)):
                # current_subset.append(nums[i])
                backtrack(i + 1, path + [nums[i]])
                # current_subset.pop()
        
        n, result = len(nums), []
        backtrack(0, [])
        return result