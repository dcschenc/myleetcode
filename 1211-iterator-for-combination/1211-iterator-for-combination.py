class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        # https://github.com/doocs/leetcode/tree/main/solution/1200-1299/1286.Iterator%20for%20Combination
        def backtrack(idx, path):
            if len(path) == combinationLength:
                self.res.append(path)
                return
            for i in range(idx, n):
                backtrack(i + 1, path + characters[i])
        
        n, self.res = len(characters), []
        backtrack(0, '')
        self.length = len(self.res)
        self.pointer = 0

    def next(self) -> str:
        ans = self.res[self.pointer]
        self.pointer += 1
        return ans

    def hasNext(self) -> bool:
        return self.pointer < self.length


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()