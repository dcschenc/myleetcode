class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        cnt = 0
        for i in range(len(strs[0])):
            for j in range(1, n):
                if strs[j-1][i] > strs[j][i]:
                    cnt += 1
                    break
        return cnt