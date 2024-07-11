class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = left = right = 0        
        for c in s:
            if c == 'L':
                left += 1
            if c == 'R':
                right += 1
            if left == right:
                cnt += 1
                left = right = 0
        return cnt

        # cnt = 0
        # hm  = {'L': 0, 'R': 0}
        # for i in range(len(s)):
        #     hm[s[i]] += 1
        #     if hm['L'] == hm['R']:
        #         cnt += 1
        #         hm['L'] = 0
        #         hm['R'] = 0
        # if hm['L'] != hm['R']:
        #     return 0
        # return cnt