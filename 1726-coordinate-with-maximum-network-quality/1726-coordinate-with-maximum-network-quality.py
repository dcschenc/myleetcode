class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1620.Coordinate%20With%20Maximum%20Network%20Quality
        hm = defaultdict(list)
        mx = -1
        for x in range(51):
            for y in range(51):
                s = 0
                for tx, ty, q in towers:
                    # d = abs(x - tx) + abs(y - ty)
                    d = math.sqrt((x - tx) ** 2 + (y - ty) ** 2)
                    if d <= radius:
                        s += math.floor(q / (1 + d))
                hm[s].append([x, y])
                mx = max(mx, s)  
        ans = hm[mx]
        ans.sort()
        return ans[0]
