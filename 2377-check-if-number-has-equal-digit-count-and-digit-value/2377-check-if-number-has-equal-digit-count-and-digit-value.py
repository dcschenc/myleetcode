class Solution:
    def digitCount(self, num: str) -> bool:
        counter = Counter(num)
        n = len(num)
        for i in range(n):            
            if counter[str(i)] != int(num[i]):
                return False
        return True