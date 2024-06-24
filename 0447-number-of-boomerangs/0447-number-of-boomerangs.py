from collections import defaultdict
class Solution:
# 对于每个点，计算其他点到该点的距离，然后按照距离进行分组计数。对每个组中的点进行两两排列组合（A n 取 2，即 n * (n - 1))）计数即可。
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        hm = defaultdict(int)
        n = len(points)
        for i in range(n):
            for j in range(n):
                if i != j:
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    dist = (x1-x2)**2 + (y1-y2)**2
                    hm[(x1, y1, dist)] += 1
        ans = 0
        for x, v in hm.items():                        
            ans += (v-1) * v
        return ans