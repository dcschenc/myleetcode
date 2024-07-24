class Solution:
    def minOperations(self, s: str) -> int:
        s = list(s)
        cnt1, cnt2 = 0, 0
        start1 = '0'
        start2 = '1'
        for c in s:
            if c != start1:
                cnt1 += 1
            if c != start2:
                cnt2 += 1
            start1 = '1' if start1 == '0' else '0'
            start2 = '0' if start2 == '1' else '1'
            
        return min(cnt1, cnt2)
            

        # ans = 0
        # for i in range(1, len(s)):
        #     if s[i] == '1' and s[i-1] == '1':
        #         s[i] = '0'
        #         ans += 1
        #     elif s[i] == '0' and s[i-1] == '0':
        #         s[i] = '1'
        #         ans += 1
        # return ans
            