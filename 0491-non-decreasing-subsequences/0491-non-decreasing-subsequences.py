class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx):
            if len(path) > 1:
                res.append(path.copy())
            if idx == n: return            
            visited = set()
            for i in range(idx, n):
                if nums[i] in visited: 
                    continue
                visited.add(nums[i])
                if len(path) > 0 and nums[i] < path[-1]:
                    continue
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        n, res, path = len(nums), [], []
        backtrack(0)
        return res

        # def backtrack(startIdx, path):
        #     if len(path) > 1:
        #         res.append(path[:])
        #     if startIdx == n:  return
            
        #     visited = set()
        #     for i in range(startIdx, n):
        #         if nums[i] in visited: 
        #             continue
        #         visited.add(nums[i])
        #         if len(path) > 0 and nums[i] < path[-1]:
        #             continue
        #         backtrack(i + 1, path + [nums[i]])

        # n, res = len(nums), []
        # backtrack(0, [])
        # return res