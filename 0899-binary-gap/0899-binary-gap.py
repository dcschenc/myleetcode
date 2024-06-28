class Solution:
    def binaryGap(self, n: int) -> int:
        # s = bin(n)[2:]
        # left = -1
        # i, n, mx = 0, len(s), 0
        # while i < n:
        #     if s[i] == '1':
        #         if left != -1:                   
        #             mx = max(mx, i - left)
        #         left = i
        #     i += 1
        # return mx

        left = -1
        mx = 0
        for i in range(31):
            if n >> i & 1 == 1:
                if left != -1:
                    mx = max(mx, i - left)
                left = i
        return mx