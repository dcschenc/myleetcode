class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counter = Counter(s)
        frequencies = counter.values()
        return len(set(frequencies)) == 1