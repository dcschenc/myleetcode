class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:      
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1625.Lexicographically%20Smallest%20String%20After%20Applying%20Operations
        # def dfs(curr):
        #     nonlocal smallest
        #     if curr in visited:
        #         return
        #     visited.add(curr)
        #     smallest = min(smallest, curr)

        #     # Apply add operation
        #     add_operation = list(curr)
        #     for i in range(1, len(add_operation), 2):
        #         add_operation[i] = str((int(add_operation[i]) + a) % 10)
        #     add_result = ''.join(add_operation)
        #     dfs(add_result)

        #     # Apply rotate operation
        #     rotate_result = curr[-b:] + curr[:-b]
        #     dfs(rotate_result)
            
        # visited = set()
        # smallest = s
        # dfs(s)
        # return smallest        

        q = deque([s])
        visited = {s}
        ans = s
        while q:
            s = q.popleft()
            if ans > s:
                ans = s
            t1 = ''.join(
                [str((int(c) + a) % 10) if i & 1 else c for i, c in enumerate(s)]
            )
            t2 = s[-b:] + s[:-b]
            for t in (t1, t2):
                if t not in visited:
                    visited.add(t)
                    q.append(t)
        return ans