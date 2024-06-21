class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 1, num
        while left <= right:
            mid = (right+left)//2
            res = mid*mid
            if res == num:
                return True
            elif res < num:
                left = mid + 1
            else:
                right = mid -1
        return False