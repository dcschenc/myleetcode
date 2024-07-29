class Robot:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.face = 'East'        
        self.pos = [0, 0]
    
    def move(self, x, y, steps):
        # print(x, y, steps)
        i = 0
        dr = {'East': (1, 0), 'North': (0, 1), 'West': (-1, 0), 'South': (0, -1)}
        dx, dy = dr[self.face]
        while i < steps and 0 <= x + dx < self.width and 0 <= y + dy < self.height:
            x, y = x + dx, y + dy
            i += 1
        return i, x, y

    def step(self, num: int) -> None:        
        x, y = self.pos
        mod = self.width * 2 + (self.height - 2) * 2
        total = num
        num = num % mod
        if total > 0 and num == 0:
            if self.face == 'East' and self.pos == [0, 0]:
                self.face = 'South'
            if self.face == 'North' and self.pos == [self.width - 1, 0]:
                self.face = 'East'
            if self.face == 'West' and self.pos == [self.width - 1, self.height - 1]:
                self.face = 'North'
            if self.face == 'South' and self.pos == [0, self.height -1]:
                self.face = 'West'
        
        steps = 0
        while steps < num:
            i, x, y = self.move(x, y, num - steps)
            steps += i
            if steps >= num:
                break
            if self.face == 'East':
                self.face = 'North'
            elif self.face == 'North':
                self.face = 'West'
            elif self.face == 'West':
                self.face = 'South'
            else:
                self.face = 'East'
        self.pos = [x, y] 

    def getPos(self) -> List[int]:
        return self.pos        

    def getDir(self) -> str:
        return self.face
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()