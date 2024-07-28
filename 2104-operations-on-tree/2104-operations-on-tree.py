class LockingTree:
    def __init__(self, parent: List[int]):
        self.children = defaultdict(list)
        self.parent = parent
        self.status = [''] * len(parent)
        for i in range(len(parent)):
            if parent[i] != -1:
                self.children[parent[i]].append(i)        

    def lock(self, num: int, user: int) -> bool:
        if self.status[num] == '':
            self.status[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if self.status[num] != '' and self.status[num] == user:
            self.status[num] = ''
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        def dfs_child(num):
            for c in self.children[num]:
                if self.status[c] != '':
                    lock_children.append(c)
                dfs_child(c)

        if self.status[num] != '':
            return False

        parent = self.parent[num]
        while parent != -1:
            if self.status[parent] != '':
                return False
            parent = self.parent[parent]

        lock_children = []
        dfs_child(num)
        if len(lock_children) == 0:
            return False
        self.status[num] = user
        for c in lock_children:
            self.status[c] = ''
        return True
        


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)