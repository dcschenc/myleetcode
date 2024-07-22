class Solution:
    def stoneGameVI(self, aliceValues: List[int], bobValues: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1686.Stone%20Game%20VI
        pairs = list([(a + b, i) for i, (a, b) in enumerate(zip(aliceValues, bobValues))])
        pairs.sort(reverse=True)
        alice = sum([aliceValues[i] for _, i in pairs[::2]])
        bob = sum([bobValues[i] for _, i in pairs[1::2]])
        if alice > bob:
            return 1
        if alice < bob:
            return -1
        return 0

