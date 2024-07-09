class SnapshotArray:
    # https://leetcode.com/problems/snapshot-array/editorial/
    def __init__(self, length: int):
        self.snap_id = 0
        self.hm = defaultdict(list)        

    def set(self, index: int, val: int) -> None:
        self.hm[index].append((self.snap_id, val))        

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1       

    def get(self, index: int, snap_id: int) -> int:
        arr = self.hm[index]
        idx = bisect_right(arr, (snap_id, inf))
        if idx > 0:
            return arr[idx-1][1]
        else:
            return 0
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)