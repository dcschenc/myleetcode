class SnakeGame:
    def __init__(self, width: int, height: int, food: List[List[int]]):
        self.m = height
        self.n = width
        self.food = food
        self.score = 0
        self.idx = 0
        self.q = deque([(0, 0)])
        self.vis = {(0, 0)}

    def move(self, direction: str) -> int:
        i, j = self.q[0]
        x, y = i, j
        match direction:
            case "U":
                x -= 1
            case "D":
                x += 1
            case "L":
                y -= 1
            case "R":
                y += 1
        if x < 0 or x >= self.m or y < 0 or y >= self.n:
            return -1
        if (
            self.idx < len(self.food)
            and x == self.food[self.idx][0]
            and y == self.food[self.idx][1]
        ):
            self.score += 1
            self.idx += 1
        else:
            self.vis.remove(self.q.pop())
        if (x, y) in self.vis:
            return -1
        self.q.appendleft((x, y))
        self.vis.add((x, y))
        return self.score

    # def __init__(self, width: int, height: int, food: List[List[int]]):
    #     self.score = 0
    #     self.m = height
    #     self.n = width
    #     self.food = food
    #     self.x, self.y = 0, 0
    #     self.cur = 0

    # def move(self, direction: str) -> int:
    #     dr = {'R': (0, 1), 'L': (0, -1), 'D': (1, 0), 'U': (-1, 0)}
    #     dx, dy = dr[direction]
    #     if 0 <= self.x + dx <= self.m - 1 and 0 <= self.y + dy <= self.n - 1:
    #         if self.cur < len(self.food) and self.x + dx == self.food[self.cur][0] and self.y + dy == self.food[self.cur][1]:                
    #             self.score += 1
    #             self.cur += 1
    #         self.x += dx
    #         self.y += dy
    #         return self.score
    #     else:
    #         return -1

        


# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)