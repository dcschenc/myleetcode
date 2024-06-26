class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        # https://leetcode.com/problems/beautiful-arrangement-ii/editorial/
        # https://www.cnblogs.com/grandyang/p/7577878.html
        ans = list(range(1, n - k))
        for i in range(k+1):
            if i % 2 == 0:
                ans.append(n - k + i//2)
            else:
                ans.append(n - i//2)

        return ans

        def backtrack(diff_arr, path):            
            if len(path) == n:
                if len(set(diff_arr)) == k:
                    return path
                else:
                    return -1           
            for j in range(1, n+1):
                if not visited[j]: 
                    diff = abs(path[-1] - j)
                    visited[j] = True
                    res = backtrack(diff_arr + [diff], path + [j])
                    if res != -1:
                        return res
                    visited[j] = False
            return -1
        
        visited = [False] * (n + 1)
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i != j:
                    diff = abs(i-j)
                    visited = [False] * (n + 1)
                    visited[i] = True
                    visited[j] = True
                    res = backtrack([diff], [i, j])
                    if res != -1:
                        return res

