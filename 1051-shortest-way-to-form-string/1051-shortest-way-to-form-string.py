class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1055.Shortest%20Way%20to%20Form%20String

        # def f(i, j):
        #     while i < m and j < n:
        #         if source[i] == target[j]:
        #             j += 1
        #         i += 1
        #     return j

        # m, n = len(source), len(target)
        # ans = j = 0
        # while j < n:
        #     k = f(0, j)
        #     if k == j:
        #         return -1
        #     j = k
        #     ans += 1
        # return ans
        
        i, count = 0, 0
        while i < len(target):
            j = 0
            found = False
            while j < len(source):
                if i < len(target) and source[j] == target[i]:
                    i += 1
                    found = True
                j += 1

            if not found: return -1
            count += 1
        return count