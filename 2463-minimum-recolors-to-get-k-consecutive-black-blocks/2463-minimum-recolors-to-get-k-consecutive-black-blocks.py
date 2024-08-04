class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        mi = cnt = blocks[:k].count('W')
        i = k
        while i < n:
            cnt -= blocks[i-k] == 'W'
            cnt += blocks[i] == 'W'
            mi = min(mi, cnt)
            i += 1
        return mi

        # ans = n + 1
        # for i in range(n-k+1):
        #     cnt = 0
        #     for j in range(k):
        #         if blocks[i+j] == 'W':
        #             cnt += 1
        #     ans = min(ans, cnt)
        # return ans