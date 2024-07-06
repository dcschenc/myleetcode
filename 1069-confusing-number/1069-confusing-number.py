class Solution:
    def confusingNumber(self, n: int) -> bool:
        hm = {0:0, 1:1, 6:9, 8:8, 9:6}
        result = 0
        origin = n
        while n != 0:
            remainder = n % 10
            if remainder not in hm:
                return False
            result = result * 10 + hm.get(remainder)
            n = n // 10
        return result != origin