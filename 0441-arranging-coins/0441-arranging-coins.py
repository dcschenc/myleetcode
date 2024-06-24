class Solution:
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right

        # cnt = 0
        # i  = 0
        # while n > 0:            
        #     i += 1
        #     n = n-i
        # if n == 0:
        #     return i
        # return i-1