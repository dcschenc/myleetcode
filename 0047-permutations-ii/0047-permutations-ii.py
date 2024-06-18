class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path):
            if len(path) == n:
                res.append(path[:])
                return
            for i in range(n):
                if visited[i] is True or i > 0 and nums[i] == nums[i - 1] and visited[i-1] is True:
                    continue                
                visited[i] = True
                backtrack(path + [nums[i]])
                visited[i] = False
        nums.sort()
        n, res = len(nums), []
        visited = [False] * n
        backtrack([])
        return res