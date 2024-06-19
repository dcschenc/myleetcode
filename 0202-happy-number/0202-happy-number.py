class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                total_sum += digit**2
            return total_sum

        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1
        
        hs = set()
        while True:
            total = 0
            while n > 0:
                total += pow(n%10, 2)
                n = n//10
            # print(sum)
            n = total
            if total == 1:
                return True
            if total in hs:
                return False
            else:
                hs.add(total)
            
        return False