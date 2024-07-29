class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:    
        n = len(s)
        presum = [0] * (n + 1)
        for i, c in enumerate(s):
            presum[i + 1] = presum[i] + (c == '*')

        left, right = [0] * n, [0] * n
        l = r = -1
        for i, c in enumerate(s):
            if c == '|':
                l = i
            left[i] = l

        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                r = i
            right[i] = r

        ans = [0] * len(queries)
        for k, (l, r) in enumerate(queries):
            i, j = right[l], left[r]
            if i >= 0 and j >= 0 and i < j:
                ans[k] = presum[j] - presum[i + 1]
        return ans
         
        # def find_candle(idx):
        #     l, r = 0, len(candles) - 1
        #     while l <= r:
        #         mid = (l + r) //2
        #         if candles[mid] < idx:
        #             l = mid + 1
        #         else:
        #             r = mid - 1                    
        #     return l            
       
        # candles = [i for i, c in enumerate(s) if c == '|']
        # ans = []
        # for i, j in queries:
        #     l = find_candle(i)
        #     r = find_candle(j + 1) - 1
        #     cnt = 0
        #     if r > l:
        #         cnt = candles[r] - candles[l]
        #         cnt = cnt - (r - l)
        #     ans.append(cnt)
        # return ans


