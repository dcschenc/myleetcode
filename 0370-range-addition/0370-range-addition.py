class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        n = length
        ans = [0] * n
        diff = [0] * (n+1)
        for start, end, incr in updates:
            diff[start] += incr
            diff[end + 1] -= incr
        # print(diff)
        for i in range(1, n+1):
            diff[i] += diff[i-1]
        # print(diff)
        return diff[:-1]
        # for i in range(n):
            # ans[i] = diff[i]
        # return ans