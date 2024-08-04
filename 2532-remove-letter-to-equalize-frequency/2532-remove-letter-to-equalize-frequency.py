class Solution:
    def equalFrequency(self, word: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/2400-2499/2423.Remove%20Letter%20To%20Equalize%20Frequency
        counter = Counter(word)
        for c in counter.keys():
            counter[c] -= 1
            if len(set([v for v in counter.values() if v != 0])) == 1:
                return True
            counter[c] += 1
        return False

        # counter = Counter(word)
        # values = list(set(counter.values()))
        # values.sort()
        # return len(values) == 1 and values[0] == 1 or len(values) == 2 and values[1] - values[0] == 1