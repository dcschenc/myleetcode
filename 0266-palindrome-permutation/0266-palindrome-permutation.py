from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        odd_count = 0
        for k, v in counter.items():
            if v%2 == 1:
                odd_count += 1
        if len(s) % 2 == 1 and odd_count == 1 or len(s)%2 == 0 and odd_count == 0:
            return True
        return False