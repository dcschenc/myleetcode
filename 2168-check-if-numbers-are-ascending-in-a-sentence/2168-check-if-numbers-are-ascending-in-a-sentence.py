class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        arr = s.split()
        prev = -1
        for w in arr:
            if w[0].isdigit():
                if int(w) <= prev:
                    return False
                prev = int(w)
        return True