class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/0900-0999/0991.Broken%20Calculator
        # https://leetcode.com/problems/broken-calculator/editorial/
        ans = 0
        while startValue < target:
            if target & 1:
                target += 1
            else:
                target >>= 1
            ans += 1
        ans += startValue - target
        return ans

        # def dfs(start, target):            
        #     if start >= target:
        #         return start - target
        #     if target % 2 == 0:
        #         return 1 + dfs(start, target//2)     
        #     else:
        #         return 1 + dfs(start, target + 1)           

        
        # ans = dfs(startValue, target)
        # return ans