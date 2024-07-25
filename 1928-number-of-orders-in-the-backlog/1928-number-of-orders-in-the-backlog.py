class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1800-1899/1801.Number%20of%20Orders%20in%20the%20Backlog
        buy, sell = [], []
        for p, q, t in orders:
            if t == 0:
                while q and sell and sell[0][0] <= p:
                    x, y = heappop(sell)
                    if q >= y:
                        q -= y
                    else:
                        heappush(sell, (x, y -q))
                        q = 0
                if q:
                    heappush(buy, (-p, q))
            else:
                while q and buy and -buy[0][0] >= p:
                    x, y = heappop(buy)
                    if q >= y:
                        q -= y
                    else:
                        heappush(buy, (x, y - q))
                        q = 0
                if q:
                    heappush(sell, (p, q))
        mod = 10**9 + 7
        return sum(v[1] for v in buy + sell) % mod

        # buy = defaultdict(int)
        # sell = defaultdict(int)
        # for p, q, t in orders:
        #     if t == 0:
        #         for sp in sorted(sell.keys()):
        #             if sp <= p:
        #                 if q >= sell[sp]:
        #                     q -= sell[sp]
        #                     sell[sp] = 0
        #                     del sell[sp]
        #                 else:
        #                     sell[sp] -= q
        #                     q = 0                            
        #                     break  
        #             else:
        #                 break              
        #         buy[p] += q
        #     else:
        #         for bp in sorted(buy.keys(), reverse=True):
        #             if bp >= p:
        #                 if q >= buy[bp]:
        #                     q -= buy[bp]
        #                     buy[bp] = 0
        #                     del buy[bp]
        #                 else:
        #                     buy[bp] -= q
        #                     q = 0
        #                     break         
        #             else:
        #                 break                   
        #         sell[p] += q
        # mod = 10 ** 9 + 7
        # return (sum(buy.values()) + sum(sell.values())) % mod