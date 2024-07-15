class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1402.Reducing%20Dishes
        satisfaction.sort(reverse=True)
        ans = s = 0
        for x in satisfaction:
            s += x
            if s <= 0:
                break
            ans += s
        return ans