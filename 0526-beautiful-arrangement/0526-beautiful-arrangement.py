from itertools import combinations_with_replacement
from collections import defaultdict
class Solution:
    def countArrangement(self, n: int) -> int:        
        def backtrack(idx):
            nonlocal ans
            if idx == n + 1:
                ans += 1
                return
            for candidate in candidates[idx]:
                if not visited[candidate]:
                    visited[candidate] = True
                    backtrack(idx + 1)
                    visited[candidate] = False            
        ans = 0
        candidates = defaultdict(list)
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i % j == 0 or j % i == 0:
                    candidates[i].append(j)
        visited = [False] * (n+1)
        backtrack(1)
        return ans