# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        left = 1
        right = 10 ** 4
        while left < right:
            mid = (left + right) // 2
            if reader.get(mid) == 2 ** 31 - 1:
                right = mid - 1
            else:
                left = mid + 1
        right = left
        left = 0
        while left <= right:
            mid = (left + right) // 2
            res = reader.get(mid)
            # print(left, right, res)
            if res == target:
                return mid
            elif res > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1