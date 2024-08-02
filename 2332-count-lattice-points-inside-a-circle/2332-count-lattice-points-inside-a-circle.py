class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2200-2299/2249.Count%20Lattice%20Points%20Inside%20a%20Circle
        ans = 0
        mx = max(x + r for x, _, r in circles)
        my = max(y + r for _, y, r in circles)
        for i in range(mx + 1):
            for j in range(my + 1):
                for x, y, r in circles:
                    dx, dy = i - x, j - y
                    if dx * dx + dy * dy <= r * r:
                        ans += 1
                        break
        return ans

        # cnt = set()
        # for x, y, r in circles:
        #     cnt.add((x, y))
        #     x1, y1 = x - r, y - r
        #     x2, y2 = x + r, y + r
        #     for i in range(x1, x2 + 1):
        #         for j in range(y1, y2 + 1):                    
        #             if (i, j) not in cnt:
        #                 if math.sqrt((i - x) ** 2 + (j - y) ** 2) <= r:
        #                     cnt.add((i, j))
        # return len(cnt)

        # cnt = Counter()
        # # cnt = set()
        # for x, y, r in circles:
        #     cnt[(x, y)] += 1
        #     for d in range(1, r + 1):
        #         cnt[(x + d, y)] += 1
        #         cnt[(x - d, y)] += 1
        #         cnt[(x, y + d)] += 1
        #         cnt[(x, y - d)] += 1
        #     for d in range(1, r // 2 + 1):
        #         cnt[(x - d, y - d)] += 1
        #         cnt[(x + d, y + d)] += 1
        #         cnt[(x - d, y + d)] += 1
        #         cnt[(x + d, y - d)] += 1

        # return len(cnt)
        
        