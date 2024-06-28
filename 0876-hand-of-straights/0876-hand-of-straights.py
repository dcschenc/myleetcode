class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        counter = Counter(hand)
        for num in sorted(counter.keys()):
            if counter[num] == 0: continue
            cnt = counter[num]
            for j in range(1, groupSize):
                if num + j not in counter or counter[num + j] < cnt:
                    return False
                counter[num + j] -= cnt
        return True