# Definition for BigArray.
# class BigArray:
#     def at(self, index: long) -> int:
#         pass
#     def size(self) -> long:
#         pass
class Solution(object):
    def countBlocks(self, nums: Optional['BigArray']) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2936.Number%20of%20Equal%20Numbers%20Blocks
        def binary_search(left, right, t):
            while left < right:
                mid = (left + right) // 2
                if nums.at(mid) != t:
                    right = mid
                else:
                    left = mid + 1
            return left
            
        count = 0
        n, i = nums.size(), 0
        while i < n:
            cur = nums.at(i)
            idx = binary_search(i, n, cur)
            count += 1
            i = idx
            # j = i + 1
            # while j < n and nums.at(j) == nums.at(i):
            #     j += 1
            # i = j
            # count += 1
        return count