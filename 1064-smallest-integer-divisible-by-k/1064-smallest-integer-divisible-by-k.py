class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1015.Smallest%20Integer%20Divisible%20by%20K
        n = 1 % k
        for i in range(1, k + 1):
            if n == 0:
                return i
            n = (n * 10 + 1) % k
        return -1