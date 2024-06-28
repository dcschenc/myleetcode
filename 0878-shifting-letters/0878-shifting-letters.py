class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/0800-0899/0848.Shifting%20Letters
        n, t = len(s), 0
        s = list(s)
        for i in range(n - 1, -1, -1):
            t += shifts[i]
            j = (ord(s[i]) - ord('a') + t) % 26
            s[i] = ascii_lowercase[j]
        return ''.join(s)

        s = list(s)
        n = len(s)
        times = 0
        base = ord('a')
        # diff = ord('z') - o
        for i in range(n-1, -1, -1):
            times += shifts[i]
            mod = times % 26
            s[i] = chr(ord('a') + (ord(s[i]) - ord('a') + mod + 26)%26)
            # idx = (ord(s[i]) + mod) %26
            # if ord(s[i]) + mod > ord('z'):
            #     s[i] = chr(ord(s[i]) + mod - ord('z') + ord('a') - 1 )
            # else:
            #     s[i] = chr(ord(s[i]) + mod)
        return ''.join(s)