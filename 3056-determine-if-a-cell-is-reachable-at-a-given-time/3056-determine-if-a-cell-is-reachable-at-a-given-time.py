class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2800-2899/2849.Determine%20if%20a%20Cell%20Is%20Reachable%20at%20a%20Given%20Time
        if sx == fx and sy == fy:
            return t != 1
        dx = abs(sx - fx)
        dy = abs(sy - fy)
        return max(dx, dy) <= t
        
        # if sx == fx and sy == fy:
        #     if t == 1:
        #         return False
        #     else:
        #         return True

        # higher = abs(sx - fx) + abs(sy - fy)
        # lower = higher - min(abs(sy - fy), abs(sx - fx))
        # return lower <= t 