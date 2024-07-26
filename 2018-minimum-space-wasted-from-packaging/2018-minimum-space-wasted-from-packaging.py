class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1889.Minimum%20Space%20Wasted%20From%20Packaging
        mod = 10**9 + 7
        ans = inf
        packages.sort()
        for box in boxes:
            box.sort()
            if packages[-1] > box[-1]:
                continue
            s = i = 0
            for b in box:
                j = bisect_right(packages, b, lo=i)
                s += (j - i) * b
                i = j
            ans = min(ans, s)
        if ans == inf:
            return -1
        return (ans - sum(packages)) % mod
