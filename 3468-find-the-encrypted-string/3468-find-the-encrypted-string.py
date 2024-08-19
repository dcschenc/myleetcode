class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/3200-3299/3210.Find%20the%20Encrypted%20String
        cs = list(s)
        n = len(s)
        for i in range(n):
            cs[i] = s[(i + k) % n]
        return "".join(cs)