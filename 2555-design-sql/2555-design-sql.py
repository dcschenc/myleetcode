class SQL:
    # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2408.Design%20SQL
    def __init__(self, names: List[str], columns: List[int]):
        self.tables = {}
        self.ids = {}
        for name, col in zip(names, columns):
            self.tables[name] = defaultdict(list)
            self.ids[name] = 0        

    def insertRow(self, name: str, row: List[str]) -> None:
        self.ids[name] += 1
        self.tables[name][self.ids[name]] = row

    def deleteRow(self, name: str, rowId: int) -> None:
        del self.tables[name][rowId]

    def selectCell(self, name: str, rowId: int, columnId: int) -> str:
        return self.tables[name][rowId][columnId-1]


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# obj.insertRow(name,row)
# obj.deleteRow(name,rowId)
# param_3 = obj.selectCell(name,rowId,columnId)