class Solution:
    def numberOfWeeks(self, milestones: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1900-1999/1953.Maximum%20Number%20of%20Weeks%20for%20Which%20You%20Can%20Work
        mx, s = max(milestones), sum(milestones)
        rest = s - mx
        if mx < rest + 1:
            return s
        else:
            return rest * 2 + 1



        