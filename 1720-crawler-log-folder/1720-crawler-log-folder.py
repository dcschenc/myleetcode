class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for s in logs:
            if s == './':
                continue
            elif s == '../':
                depth -= 1
                depth = max(0, depth)
            else:
                depth += 1
        return depth