class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        counter = Counter(ranks)
        if len(set(suits)) == 1:
            return "Flush"
        if any(v >= 3 for v in counter.values()):
            return 'Three of a Kind'
        if any(v >= 2 for v in counter.values()):
            return "Pair"
        return "High Card"