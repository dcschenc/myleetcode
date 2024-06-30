class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def get_num(path):
            ans = 0
            # path.reverse()
            for i, d in enumerate(path):
                ans = ans * 10  +  d
            return ans

        def backtrack(idx, path):
            if idx == n + 1:
                ans.append(get_num(path))
                return
            for i in range(0, 10):
                if idx == 1 and i == 0: 
                    continue
                if idx == 1 or idx > 1 and abs(i - path[-1]) == k:
                    backtrack(idx + 1, path + [i])
            
        ans = []
        backtrack(1, [])
        # ans.sort()
        return ans