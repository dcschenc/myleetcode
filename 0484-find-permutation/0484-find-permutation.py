class Solution:
    # https://github.com/doocs/leetcode/tree/main/solution/0400-0499/0484.Find%20Permutation
    def findPermutation(self, s: str) -> List[int]:
        n = len(s)
        ans = list(range(1, n + 2))
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == 'D':
                j += 1
            ans[i : j + 1] = ans[i : j + 1][::-1]
            i = max(i + 1, j)
        return ans
