class Solution:
    def distinctIntegers(self, n: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2549.Count%20Distinct%20Numbers%20on%20Board
        return max(1, n - 1)