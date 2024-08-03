class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        d = {" ": " "}
        i = 0
        for c in key:
            if c not in d:
                d[c] = ascii_lowercase[i]
                i += 1
        return "".join(d[c] for c in message)

        # d = {}
        # cur = ord('a')
        # for c in key:
        #     if c not in d and c != ' ': 
        #         d[c] = chr(cur)
        #         cur += 1
        # ans = ''
        # for c in message:
        #     if c == ' ':
        #         ans += c
        #     else:
        #         ans += d[c]
        # return ans
