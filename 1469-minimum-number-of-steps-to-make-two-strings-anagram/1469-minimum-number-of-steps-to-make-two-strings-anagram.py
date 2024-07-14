class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter1, counter2 = Counter(s), Counter(t)
        n = len(s)
        common = 0
        for k, v in counter2.items():
            if k in counter1:
                common += min(v, counter1[k])
        return n - common