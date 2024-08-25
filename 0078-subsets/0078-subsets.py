class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            result.append(path[:])
            if start == n: 
                return            
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])
        
        n, result = len(nums), []
        backtrack(0, [])
        return result