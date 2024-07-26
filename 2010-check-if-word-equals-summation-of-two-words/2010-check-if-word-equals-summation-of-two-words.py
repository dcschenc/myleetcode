class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        base = ord('a')
        num1, num2, target = '', '', ''
        for c in firstWord:
            num1 += str(ord(c) - base)
        for c in secondWord:
            num2 += str(ord(c) - base)
        for c in targetWord:
            target += str(ord(c) - base)
        return int(num1) + int(num2) == int(target)