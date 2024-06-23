class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/0400-0499/0402.Remove%20K%20Digits
        stk = []
        remain = len(num) - k
        for c in num:
            while k and stk and stk[-1] > c:
                stk.pop()
                k -= 1
            stk.append(c)
        return ''.join(stk[:remain]).lstrip('0') or '0'
        
