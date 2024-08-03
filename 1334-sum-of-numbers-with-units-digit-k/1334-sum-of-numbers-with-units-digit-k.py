import sys
class Solution:
    def minimumNumbers(self, num: int, k: int) -> int:
        if num == 0:
            return 0
        for i in range(1, num + 1):
            cur = num - k * i
            if cur >= 0 and cur % 10 == 0:
                return i
        return -1

        # @cache
        # def backtrack(cur):
        #     if cur > num: return float('inf')
        #     if cur == num: return 0
        #     res = float('inf')
        #     for candidate in range(k, num - cur + 1, 10):
        #         if candidate == 0: continue
        #         res = min(res, 1 + backtrack(cur + candidate))
        #     return res
        
        # if not num: return num   
        # ans = backtrack(0) 
        # if ans == float('inf'): return -1
        # return ans

        # # sys.setrecursionlimit(10**6)
        # def backtrack(cur, cnt):
        #     if cur == 0:
        #         ans[0] = min(ans[0], cnt)
        #         return True
        #     if cur < 0: 
        #         return False
        #     i = 1
        #     while i * 10 < cur:
        #         i += 1
        #     for j in range(i, -1, -1):
        #         if (k + 10 * j) == 0: continue
        #         if backtrack(cur - (k + 10 * j), cnt + 1):
        #             return True
        #         # break
        #     return False

        # if num == 0: return 0
        # if k == 0 and (num < 10 or num >= 10 and num% 10 != 0): return -1
        # ans =[float('inf')]
        # backtrack(num, 0)
        # return ans[0] if ans[0] != float('inf') else -1