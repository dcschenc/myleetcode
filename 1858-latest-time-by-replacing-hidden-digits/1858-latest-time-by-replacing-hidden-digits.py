class Solution:
    def maximumTime(self, time: str) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1736.Latest%20Time%20by%20Replacing%20Hidden%20Digits
        t = list(time)
        if t[0] == '?':
            t[0] = '1' if '4' <= t[1] <= '9' else '2'
        if t[1] == '?':
            t[1] = '3' if t[0] == '2' else '9'
        if t[3] == '?':
            t[3] = '5'
        if t[4] == '?':
            t[4] = '9'
        return ''.join(t)
        
        ans = ''
        for i, c in enumerate(time):
            if c != '?':
                ans += c
            else:
                if i == 0:
                    if time[1] in '?0123':
                        ans += '2'
                    else:
                        ans += '1'
                elif i == 1:
                    if ans[-1] == '2':
                        ans += '3'
                    else:
                        ans += '9'
                elif i == 2:
                    ans += c
                elif i == 3:
                    ans += '5'
                elif i == 4:
                    ans += '9'
        return ans
