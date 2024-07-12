class Solution:
    def toHexspeak(self, num: str) -> str:
        ans = ''
        for c in hex(int(num))[2:].upper():
            if c == '0':
                c = 'O'
            elif c == '1':
                c = 'I'
            ans += c
            if c not in 'ABCDEFIO':
                return 'ERROR'
        return ans
        