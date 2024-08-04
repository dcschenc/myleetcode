class LUPrefix:

    def __init__(self, n: int):
        self.n = n
        self.hm = set()
        self.cur = 0        

    def upload(self, video: int) -> None:
        self.hm.add(video)
        if video == self.cur + 1:
            while video in self.hm:
                video += 1
            self.cur = video - 1

    def longest(self) -> int:
        return self.cur
        
        # for i in range(1, self.n + 1):
        #     if i not in self.hm:
        #         return i - 1
        # return self.n


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()