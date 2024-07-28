class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def backtrack(idx, path):
            if idx == n:
                if path not in nums:
                    return path
            for i in range(idx, n):
                res = backtrack(idx + 1, path + '0')
                if res != '-1':
                    return res
                res = backtrack(idx + 1, path + '1')
                if res != '-1':
                    return res
            return '-1'
        n = len(nums)
        return backtrack(0, '')

