class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return len(counter.values()) == len(set(counter.values()))
        # hm = {}
        # for n in arr:
            # hm[n] = 1 + hm.get(n, 0)
            # if v not in occur:
            #     hm[v] = 1
            # else:
            #     hm[v] += 1
        # values = hm.values()
        # return len(set(values)) == len(values)
