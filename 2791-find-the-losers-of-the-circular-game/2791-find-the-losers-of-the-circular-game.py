class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:  
        vis = [False] * n
        i, p = 0, 1
        while not vis[i]:
            vis[i] = True
            i = (i + p * k) % n
            p += 1
        return [i + 1 for i in range(n) if not vis[i]]
             
        # s = set()
        # cur = 1
        # i = 0
        # while True:
        #     cur = (cur + k * i - 1) % n + 1
        #     if cur in s:
        #         break
        #     s.add(cur)
        #     i += 1

        # ans = []
        # for i in range(1, n + 1):
        #     if i not in s:
        #         ans.append(i)
        # return ans
