class Solution:
    def minDays(self, n: int) -> int:
        @cache
        def dfs(n: int) -> int:
            if n < 2:
                return n
            return 1 + min(n % 2 + dfs(n // 2), n % 3 + dfs(n // 3))

        return dfs(n)

        queue = deque([(n, 0)])  # (current number of oranges, number of days)
        visited = set([n])       # To avoid revisiting the same number of oranges

        while queue:
            oranges, days = queue.popleft()
            
            if oranges == 0:
                return days
            
            # If we can eat one orange
            if oranges - 1 not in visited:
                visited.add(oranges - 1)
                queue.append((oranges - 1, days + 1))
            
            # If the current number of oranges is divisible by 2
            if oranges % 2 == 0 and oranges // 2 not in visited:
                visited.add(oranges // 2)
                queue.append((oranges // 2, days + 1))
            
            # If the current number of oranges is divisible by 3
            if oranges % 3 == 0 and oranges - 2 * (oranges // 3) not in visited:
                visited.add(oranges - 2 * (oranges // 3))
                queue.append((oranges - 2 * (oranges // 3), days + 1))

        # @cache
        # def dfs(i):
        #     if i == 0:
        #         return 0
        #     ans = 1 + dfs(i-1)
        #     if i % 2 == 0:
        #         ans = min(ans, 1 + dfs(i // 2))
        #     if i % 3 == 0:
        #         ans = min(ans, 1 + dfs(i - 2 * (i // 3)))
        #     return ans

        
        # ans = dfs(n)
        # return ans
