class DetectSquares:
    # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2013.Detect%20Squares
    def __init__(self):
        self.cnt = defaultdict(Counter)

    def add(self, point: List[int]) -> None:
        x, y = point
        self.cnt[x][y] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        if x1 not in self.cnt:
            return 0
        ans = 0
        for x2 in self.cnt.keys():
            if x2 != x1:
                d = x2 - x1
                ans += self.cnt[x2][y1] * self.cnt[x1][y1 + d] * self.cnt[x2][y1 + d]
                ans += self.cnt[x2][y1] * self.cnt[x1][y1 - d] * self.cnt[x2][y1 - d]
        return ans


    # def __init__(self):
    #     self.points_x = defaultdict(list)
    #     self.points_y = defaultdict(list)

    # def add(self, point: List[int]) -> None:
    #     x, y = point
    #     self.points_x[x].append(point)
    #     self.points_y[y].append(point)
        

    # def count(self, point: List[int]) -> int:
    #     x1, y1 = point
    #     ans = 0
    #     for x2, y2 in self.points_x[x1]:
    #         if y2 == y1: continue
    #         for x3, y3 in self.points_y[y2]:
    #             for x4, y4 in self.points_y[y1]:
    #                 if x3 == x4 and abs(x1 - x4) == abs(y1 - y2) and x3 != x1 and x4 != x2:
    #                     ans += 1
    #     return ans


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)