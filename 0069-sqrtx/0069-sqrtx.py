class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while left <= right:
            mid = left + (right - left) // 2
            y = mid * mid
            if y == x:
                return mid
            elif y < x:
                # if (mid+1) * (mid+1) > x:
                #     return mid
                # else:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1