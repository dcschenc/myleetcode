class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        quarter_point = n // 4

        for i in range(quarter_point, n):
            if arr[i] == arr[i - quarter_point]:
                return arr[i]

        # def check_target(mid):
        #     # print(mid)
        #     target = arr[mid]
        #     i = mid
        #     while i >= 0:
        #         if arr[i] != target:
        #             break
        #         i -= 1
        #     j = mid
        #     while j < len(arr):
        #         if arr[j] != target:
        #             break
        #         j += 1
        #     if j - i - 1 > len(arr)/4:
        #         return target
        #     return -1

        # left, right = 0, len(arr) - 1
        # mid = (left + right)//2
        # res = check_target(mid)
        # if res != -1:
        #     return res
        # mid_left = (left + mid - 1)//2
        # res = check_target(mid_left)
        # if res != -1:
        #     return res
        # mid_right = (right + mid + 1)//2
        # res = check_target(mid_right)
        # return res