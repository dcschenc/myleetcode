class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/1400-1499/1400.Construct%20K%20Palindrome%20Strings
        counter = Counter(s)
        odds = len([v for v in counter.values() if v % 2 == 1])
        if len(s) < k or odds > k:
            return False
        return True