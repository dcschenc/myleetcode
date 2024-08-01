class Solution:
    def countEven(self, num: int) -> int:
        ans = 0
        for x in range(1, num + 1):
            s = 0
            while x:
                s += x % 10
                x //= 10
            ans += s % 2 == 0
        return ans
        
        total = 0
        for n in range(1, num + 1):
            if sum(int(d) for d in str(n)) % 2 == 0:
                total += 1
        return total