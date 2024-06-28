class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        digits = str(n)
        m = len(digits)
        for a in permutations(digits, m):
            if a[0] != '0':
                cur = int(''.join(a))
                # log = math.log(cur, 2)
                # if int(log) == log:
                if cur & (cur - 1) == 0 and cur != 0:
                    return True
        return False