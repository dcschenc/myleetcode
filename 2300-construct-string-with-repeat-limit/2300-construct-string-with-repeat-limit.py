class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:        
        counter, ans = Counter(s), ''
        while len(counter) > 0:
            keys = list(counter.keys())
            keys.sort(reverse=True)
            cur = keys[0]
            if counter[cur] <= repeatLimit:
                ans += cur * counter[cur]
                del counter[cur]
            else:
                ans += cur * repeatLimit
                counter[cur] -= repeatLimit
                if len(keys) < 2:
                    return ans
                nxt = keys[1]
                ans += nxt
                counter[nxt] -= 1 
                if counter[nxt] == 0:
                    del counter[nxt]
        return ans