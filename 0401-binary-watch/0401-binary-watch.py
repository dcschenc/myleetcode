class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:    
        # def dfs(num, hours, res):
        #     if hours > num : 
        #         return
        #     for hour in combinations([1, 2, 4, 8], hours):
        #         hs = sum(hour)
        #         if hs >= 12 : 
        #             continue
        #         for minu in combinations([1, 2, 4, 8, 16, 32], num - hours):
        #             mins = sum(minu)
        #             if mins >= 60 : 
        #                 continue
        #             res.append("%d:%02d" % (hs, mins))
        #     dfs(num, hours + 1, res)

        # res = []
        # dfs(num, 0, res)
        # return res

        res = []
        for h in range(12):
            for m in range(60):
                # if (bin(h) + bin(m)).count('1') == num:
                if h.bit_count() + m.bit_count() == num:
                    res.append('{:d}:{:02d}'.format(h, m))
        return res
