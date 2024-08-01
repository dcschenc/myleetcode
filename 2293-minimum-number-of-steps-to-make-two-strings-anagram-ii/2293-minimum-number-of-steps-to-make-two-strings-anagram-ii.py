class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counter1, counter2 = Counter(s), Counter(t)
        keys = set(counter1.keys()) | set(counter2.keys())
        total = 0
        for k in keys:
            if k in counter1 and k in counter2:
                total += abs(counter1[k] - counter2[k])
            elif k in counter1:
                total += counter1[k]
            else:
                total += counter2[k]
        return total
                
        