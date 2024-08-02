class Solution:
    def largestGoodInteger(self, num: str) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2264.Largest%203-Same-Digit%20Number%20in%20String
        for i in range(9, -1, -1):
            if (s := str(i) * 3) in num:
                return s
        return ""

        ans = ''
        i, n = 2, len(num)
        while i < n:
            if num[i-2] == num[i-1] == num[i]:
                if ans == '' or int(ans) < int(num[i-2:i+1]):
                    ans = num[i-2:i+1]
            i += 1
        return ans