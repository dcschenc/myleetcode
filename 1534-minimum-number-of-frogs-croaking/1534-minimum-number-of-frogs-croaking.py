class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1419.Minimum%20Number%20of%20Frogs%20Croaking
        if len(croakOfFrogs) % 5 != 0:
            return -1
        idx = {c: i for i, c in enumerate('croak')}
        cnt = [0] * 5
        ans = x = 0
        for i in map(idx.get, croakOfFrogs):
            cnt[i] += 1
            if i == 0:
                x += 1
                ans = max(ans, x)
            else:
                if cnt[i - 1] == 0:
                    return -1
                cnt[i - 1] -= 1
                if i == 4:
                    x -= 1
        return -1 if x else ans


        hm = defaultdict(int)
        ans, cur = 0, 0
        for c in croakOfFrogs:            
            if c == 'c':        
                cur += 1        
                hm[c] += 1                
            elif c == 'r':
                if hm['c'] == 0:
                    return -1
                hm['c'] -= 1
                hm['cr'] += 1
            elif c == 'o':
                if hm['cr'] == 0:
                    return -1
                hm['cr'] -= 1
                hm['cro'] += 1
            elif c == 'a':
                if hm['cro'] == 0:
                    return -1
                hm['cro'] -= 1
                hm['croa'] += 1
            elif c== 'k':
                if hm['croa'] == 0:
                    return -1
                hm['croa'] -= 1
                cur -= 1
           
            ans = max(ans, cur)
        
        return ans if cur == 0 else -1