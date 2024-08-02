class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2240.Number%20of%20Ways%20to%20Buy%20Pens%20and%20Pencils
        mx_1, mx_2 = total // cost1,  total // cost2
        ans = 0
        for i in range(mx_1 + 1):
            ans += (total - cost1 * i) // cost2 + 1
        # for i in range(mx_2 + 1):
        #     ans += (total - cost2 * i) // cost1 + 1
  
        return ans