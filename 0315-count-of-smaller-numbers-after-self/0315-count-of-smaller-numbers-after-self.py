import bisect
from sortedcontainers import SortedList

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ########## O(nlogn)  BST ###########
        sorted_list = SortedList()
        result = []

        for num in reversed(nums):
            result.append(sorted_list.bisect_left(num))
            sorted_list.add(num)

        return reversed(result)

        def mergeSort(enumerated_nums):
            if len(enumerated_nums) <= 1:
                return enumerated_nums, [0]  # Base case

            middle = len(enumerated_nums) // 2
            left, left_count = mergeSort(enumerated_nums[:middle])
            right, right_count = mergeSort(enumerated_nums[middle:])

            merged = []
            merged_count = []
            i, j = 0, 0

            while i < len(left) or j < len(right):
                if j == len(right) or (i < len(left) and left[i][1] <= right[j][1]):
                    merged.append(left[i])
                    merged_count.append(left_count[i] + j)
                    i += 1
                else:
                    merged.append(right[j])
                    merged_count.append(right_count[j])
                    j += 1

            return merged, merged_count

        enumerated_nums = list(enumerate(nums))
        result = mergeSort(enumerated_nums)[1]

        return result