class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:        
        return sum(w.startswith(pref) for w in words)        
        total = 0
        for w in words:
            if w.startswith(pref):
                total += 1
        return total