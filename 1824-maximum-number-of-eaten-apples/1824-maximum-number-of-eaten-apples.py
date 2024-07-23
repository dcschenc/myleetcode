from sortedcontainers import SortedDict
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1700-1799/1705.Maximum%20Number%20of%20Eaten%20Apples
        n = len(days)
        i = ans = 0
        q = []
        while i < n or q:
            if i < n and apples[i]:
                heappush(q, (i + days[i] - 1, apples[i]))
            while q and q[0][0] < i:
                heappop(q)
            if q:
                day, qty = heappop(q)
                qty -= 1
                ans += 1
                if qty and day > i:
                    heappush(q, (day, qty))
            i += 1
        return ans
        
        # to_eat = SortedDict()
        # n, ans = len(apples), 0
        # for i in range(n):
        #     if apples[i] != 0:
        #         day = int(i + days[i])
        #         if day not in to_eat:
        #             to_eat[day] = apples[i]
        #         else:
        #             to_eat[day] += apples[i]            
        #     if len(to_eat) > 0:
        #         key, val = to_eat.peekitem(index=0)
        #         to_eat.popitem(index=0)
        #         ans += 1
        #         val -= 1
        #         if val > 0:
        #             to_eat[key] = val                

        #     if i + 1 in to_eat:
        #         del to_eat[i + 1]
            
        # i = n
        # while len(to_eat) > 0:            
        #     key, val = to_eat.peekitem(index=0)
        #     to_eat.popitem(index=0)
        #     ans += 1
        #     val -= 1
        #     if val > 0:
        #         to_eat[key] = val
        #     if i + 1 in to_eat:
        #         del to_eat[i + 1]
        #     if len(to_eat) == 0:
        #         break
        #     i += 1
        # return ans
        