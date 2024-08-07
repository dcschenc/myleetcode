class Solution:
    def monkeyMove(self, n: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2550.Count%20Collisions%20of%20Monkeys%20on%20a%20Polygon
        mod = 10**9 + 7
        return (pow(2, n, mod) - 2) % mod
