class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            res.append(path[:])
            if start == n: 
                return            
            for i in range(start, n):
                if i > 0 and nums[i] == nums[i-1] and visited[i-1] is False:
                    continue
                visited[i] = True
                backtrack(i + 1, path + [nums[i]])          
                visited[i] = False

        n, res = len(nums), []
        visited = [False] * n
        nums.sort()
        backtrack(0, [])
        return res

        def backtrack(nums, curr):
            res.append(curr)
            for i, v in enumerate(nums):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                backtrack(nums[i+1:], curr+[v])
        
        res = []
        nums.sort()
        backtrack(nums, [])
        return res