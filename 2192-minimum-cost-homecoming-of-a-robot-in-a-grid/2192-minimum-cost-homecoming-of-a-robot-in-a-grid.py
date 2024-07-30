class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:        
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2087.Minimum%20Cost%20Homecoming%20of%20a%20Robot%20in%20a%20Grid
        ans = 0
        if startPos[0] < homePos[0]:
            ans += sum(rowCosts[startPos[0] + 1: homePos[0] + 1])
        else:
            ans += sum(rowCosts[homePos[0]:startPos[0]])
        
        if startPos[1] < homePos[1]:
            ans += sum(colCosts[startPos[1] + 1: homePos[1] + 1])
        else:
            ans += sum(colCosts[homePos[1]: startPos[1]])

        return ans