class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        def dfs(u):
            if u == 0:
                return ['']
            if u == 1:
                return ['0', '1', '8']
            ans = []
            for v in dfs(u - 2):
                for l, r in ('11', '88', '69', '96'):
                    ans.append(l + v + r)
                if u != n:
                    ans.append('0' + v + '0')
            return ans

        return dfs(n)
        
        # def generate(n, m):
        #     if n == 0:
        #         return [""]
        #     if n == 1:
        #         return ["0","1","8"]            
            
        #     prev_res = generate(n-2, m)           

        #     hm = [('9', '6'), ('8','8'),  ('6','9'), ('0', '0'), ('1','1')]
        #     res = []
        #     for s in prev_res:
        #         for l, r in hm:
        #             if l == '0' and n == m:
        #                 continue
        #             res.append(l+s+r) 
        #     return res

        # return generate(n, n)
        