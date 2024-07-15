class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        def get_steps(x):
            steps = 0
            while x != 1:
                if x % 2 == 0:
                    x = x // 2
                else:
                    x = 3 * x + 1
                steps += 1
            return steps
        
        return sorted(range(lo, hi + 1), key=get_steps)[k-1]