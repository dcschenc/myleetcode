class ThroneInheritance:
    # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1600.Throne%20Inheritance
    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.deaths = set()
        self.king = kingName
        

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)        

    def death(self, name: str) -> None:
        self.deaths.add(name)
        

    def getInheritanceOrder(self) -> List[str]:
        def dfs(node):
            if node not in self.deaths:
                ans.append(node)
            for c in self.graph[node]:
                dfs(c)
        ans = []
        dfs(self.king)
        return ans
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()