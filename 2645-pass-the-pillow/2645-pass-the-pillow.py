class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        cnt = time // (n - 1)
        mod = time % (n - 1)
        if cnt % 2 == 1:
            mod = n - mod 
        else:
            mod = mod + 1
        return mod