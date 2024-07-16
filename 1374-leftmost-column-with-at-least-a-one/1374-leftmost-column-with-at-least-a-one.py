# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:
from bisect import bisect_left

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: "BinaryMatrix") -> int:
        m, n = binaryMatrix.dimensions()  # Get the dimensions of the binary matrix
        ans = n  # Initialize the answer to the number of columns

        for i in range(m):  # Iterate over each row
            # Perform a binary search to find the leftmost '1' in the current row
            j = bisect_left(range(n), 1, key=lambda k: binaryMatrix.get(i, k))
            ans = min(ans, j)  # Update the answer with the minimum column index found

        # If ans is still n, it means there are no '1's in any row, so return -1
        # Otherwise, return the leftmost column index with at least one '1'
        return -1 if ans >= n else ans
