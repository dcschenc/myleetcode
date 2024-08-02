class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        cnt = 0
        for w in words:
            if s.startswith(w):
                cnt += 1
        return cnt