class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(cnt, path):
            if cnt == n:
                res.append(path[:])
            for i in range(n):
                if visited[i] is True: 
                    continue
                visited[i] = True
                backtrack(cnt + 1, path + [nums[i]])
                visited[i] = False
        
        n, res = len(nums), []
        visited = [False] * n
        backtrack(0, [])
        return res



        def backtrack(nums, cnt, path):
            if cnt == n:
                res.append(path[:])
                return
            for i in range(len(nums)):                
                backtrack(nums[:i] + nums[i+1:], cnt + 1, path + [nums[i]])
               
        
        res = []
        n = len(nums)
        backtrack(nums, 0, [])
        return res

        def backtrack(nums, arr):
            if len(arr) == n:
                res.append(arr[:])
                return
            for i in range(len(nums)):
                arr.append(nums[i])
                backtrack(nums[:i] + nums[i+1:], arr)
                arr.pop()
        
        res = []
        n = len(nums)
        backtrack(nums, [])
        return res