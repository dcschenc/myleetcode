class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        return max(
            number[:i] + number[i + 1 :] for i, d in enumerate(number) if d == digit
        )
        
        i, n = 0, len(number)
        cnt = number.count(digit)
        while i < n:
            if number[i] == digit:
                cnt -= 1
                if i + 1 == n:
                    return number[:-1]
                else:
                    if number[i + 1] > digit or cnt == 0:
                        return number[:i] + number[i + 1:]
            i += 1