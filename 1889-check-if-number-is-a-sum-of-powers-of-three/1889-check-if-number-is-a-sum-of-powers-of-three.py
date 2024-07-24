class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        @cache
        def dfs(cur, i):
            if cur == n:
                return True
            if i == len(choices):
                return False            
            if cur + choices[i] > n:
                return False
            if dfs(cur + choices[i], i + 1) or dfs(cur, i + 1):
                return True            
            return False       

        choices = []
        x = 1
        while x <= n:
            choices.append(x)
            x *= 3
        return dfs(0, 0)

        # @cache
        # def dfs(cur, candidates):
        #     if cur == 0:
        #         return True
        #     if len(candidates) == 0:
        #         return False            
        #     for i, x in enumerate(candidates):
        #         if cur >= x:
        #             if dfs(cur - x, candidates[:i] + candidates[i+1:]):
        #                 return True
        #         else:
        #             break
        #     return False
        