# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.nums = []
        self.idx = 0        
        def get_values(curList):
            cur = []
            for item in curList:
                if item.isInteger():
                    cur.append(item.getInteger())
                else:
                    cur.extend(get_values(item.getList()))
            return cur
        self.nums = get_values(nestedList)        
    
    def next(self) -> int:
        # if self.hasNext():
            # return self.nums.pop(0)
        val =  self.nums[self.idx]
        self.idx += 1
        return val
    
    def hasNext(self) -> bool:
        # return len(self.nums) > 0
        return self.idx < len(self.nums)
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())