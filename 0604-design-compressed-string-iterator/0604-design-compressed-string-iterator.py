class StringIterator:
    # https://github.com/doocs/leetcode/tree/main/solution/0600-0699/0604.Design%20Compressed%20String%20Iterator
    def __init__(self, compressedString: str):
        self.s = compressedString
        self.pos = 0
        self.cnt = 0        
        self.c = ''
        self.n = len(self.s)

    def next(self) -> str:
        if self.cnt <= 0:
            if self.pos < self.n:
                self.c = self.s[self.pos]
                self.pos += 1
                cnt = 0
                while self.pos < self.n and self.s[self.pos].isdigit():
                    cnt = cnt * 10 + int(self.s[self.pos])
                    self.pos += 1
                self.cnt = cnt
            else:
                return ' '
        self.cnt -= 1
        return self.c

    def hasNext(self) -> bool:
        if self.cnt == 0 and self.pos == self.n:
            return False
        return True
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()