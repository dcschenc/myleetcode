class Solution:
    def minimizeStringValue(self, s: str) -> str:
        # https://github.com/doocs/leetcode/tree/main/solution/3000-3099/3081.Replace%20Question%20Marks%20in%20String%20to%20Minimize%20Its%20Value
        cnt = Counter(s)
        pq = [(cnt[c], c) for c in string.ascii_lowercase]
        heapify(pq)
        t = []
        for _ in range(s.count("?")):
            v, c = pq[0]
            t.append(c)
            heapreplace(pq, (v + 1, c))
        t.sort()
        cs = list(s)
        j = 0
        for i, c in enumerate(s):
            if c == "?":
                cs[i] = t[j]
                j += 1
        return "".join(cs)
