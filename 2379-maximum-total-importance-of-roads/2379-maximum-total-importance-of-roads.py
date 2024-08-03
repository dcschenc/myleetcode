class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        hm = defaultdict(int)
        for u, v in roads:
            hm[u] += 1
            hm[v] += 1
        ans = 0
        for k, v in sorted(hm.items(), key=lambda x:x[1], reverse=True):
            ans += n * v
            n -= 1
        return ans