class Solution:
    def minimumLength(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3200-3299/3223.Minimum%20Length%20of%20String%20After%20Operations
        counter = Counter(s)
        total = 0
        for k, v in counter.items():
            if v % 2 == 1:
                total += 1
            else:
                total += 2
        return total