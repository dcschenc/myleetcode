class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        min_area = inf
        dict_x = defaultdict(set)
        for x, y in points:
            dict_x[x].add(y)
        dict_x = {x: set_y for x, set_y in dict_x.items() if len(set_y) > 1}
        for x1, x2 in combinations(dict_x.keys(), 2):
            for y1, y2 in combinations(dict_x[x1] & dict_x[x2], 2):
                min_area = min(min_area, abs(x1 - x2) * abs(y1 - y2))
        return min_area if min_area < inf else 0
        
        ans = float('inf')
        points.sort()
        n = len(points)
        hm_x, hm_y = defaultdict(list), defaultdict(list)
        for x, y in points:
            hm_x[x].append((x, y))
            hm_y[y].append((x, y))

        for i, (x1, y1) in enumerate(points):
            for x2, y2 in hm_y[y1]:
                if x2 < x1:
                    for x3, y3 in hm_x[x2]:
                        if y3 != y2:
                            for x4, y4 in hm_y[y3]:
                                if x1 - x2 == x4 - x3 and y1 - y4 == y2 - y3:
                                    ans = min(ans, abs(x1-x2) * abs(y1-y4))

            # for j in range(i):
            #     x2, y2 = points[j]
            #     if y2 == y1:
            #         for x3, y3 in hm_x[x2]:
            #             if y3 != y2:
            #                 for x4, y4 in hm_y[y3]:
            #                     if x1 - x2 == x4 - x3 and y1 - y4 == y2 - y3:
            #                         ans = min(ans, abs(x1-x2) * abs(y1-y4))

        return ans if ans != float('inf') else 0

