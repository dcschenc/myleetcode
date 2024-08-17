class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3113.Find%20the%20Number%20of%20Subarrays%20Where%20Boundary%20Elements%20Are%20Maximum
        stk = []
        ans = 0
        for x in nums:
            while stk and stk[-1][0] < x:
                stk.pop()
            if not stk or stk[-1][0] > x:
                stk.append([x, 1])
            else:
                stk[-1][1] += 1
            ans += stk[-1][1]
        return ans