class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3200-3299/3200.Maximum%20Height%20of%20a%20Triangle
        ans = 0
        for k in range(2):
            c = [red, blue]
            i, j = 1, k
            while i <= c[j]:
                c[j] -= i
                j ^= 1
                ans = max(ans, i)
                i += 1
        return ans