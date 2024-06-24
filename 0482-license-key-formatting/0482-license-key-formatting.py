class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        n = len(s)
        count = 0
        ans = ['']
        for i in reversed(range(n)):
            if s[i] != '-':
                ans += s[i].upper()
                count = count + 1
                if count == k:
                    count = 0
                    ans += '-'
     
        # Make sure the output doesn't start with a dash
        if (len(ans) > 0 and ans[len(ans)-1] == '-'):
            ans = ans[:-1]
        ans = ans[::-1]
        return "".join(ans)

        # segments = s.split('-')
        # s = ''.join(segments)
        # n = len(s)
        # first_len = n % k
        # if first_len == 0:
        #     first_len = k
        # res = ''
        # cnt = 0
        # for i in range(n):
        #     res += s[i].upper()
        #     cnt += 1
        #     if i != 0 and cnt % k == 0 or (i+1) == first_len:
        #         res += '-'
        #         cnt = 0
        # res = res.strip('-')
        # return res
