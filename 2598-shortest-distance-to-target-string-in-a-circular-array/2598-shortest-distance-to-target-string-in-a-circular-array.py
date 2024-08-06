class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        for i in range(n + 1):
            if words[(startIndex + i) % n] == target or words[(startIndex - i + n) % n] == target:
                return i
        return -1