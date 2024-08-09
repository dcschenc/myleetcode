class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        def backtrack(idx, cur):              
            ans[0] = max(ans[0], cur) if ans[0] is not None else cur
            for i in range(idx, n):
                backtrack(i + 1, cur * nums[i])
        
        ans, n = [None], len(nums)
        for i in range(n):
            backtrack(i+1, nums[i])
        return ans[0]

        def backtrack(idx, path):
            if len(path) != 0:
                val = 1
                for num in path:
                    val *= num         
                ans[0] = max(ans[0], val) if ans[0] is not None else val
            for i in range(idx, n):
                backtrack(i + 1, path + [nums[i]])
        
        ans, n = [None], len(nums)
        backtrack(0, [])
        return ans[0]