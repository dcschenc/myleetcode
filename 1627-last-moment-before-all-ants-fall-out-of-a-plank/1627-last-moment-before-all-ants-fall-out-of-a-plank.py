class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        # https://leetcode.com/problems/last-moment-before-all-ants-fall-out-of-a-plank/editorial/
        # https://github.com/doocs/leetcode/tree/main/solution/1500-1599/1503.Last%20Moment%20Before%20All%20Ants%20Fall%20Out%20of%20a%20Plank
        ans = 0
        for i in left:
            ans = max(ans, i)
        for i in right:
            ans = max(ans, n - i)
        return ans