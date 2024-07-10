from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counter = Counter(text)
        result = float('inf')
        for c in 'balloon':
            if c == 'l' or c == 'o':
                result = min(result, counter.get(c, 0)//2)
            else:
                result = min(result, counter.get(c, 0))
        return result 
