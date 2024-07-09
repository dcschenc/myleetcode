from collections import defaultdict 
class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        hm = defaultdict(list)
        visited = list(zip(username, website, timestamp))
        visited.sort(key=lambda x: x[2])
        for u, w, t in visited:
            hm[u].append(w)
        pattern_hm = defaultdict(set)
        # pattern_hm = Counter()
        for u, w in hm.items():
            for i in range(len(w)):
                for j in range(i+1, len(w)):
                    for k in range(j+1, len(w)):
                        p = (w[i], w[j], w[k])
                        pattern_hm[p].add(u)
                        # pattern_hm[p] += 1
        sorted_items = sorted(pattern_hm.items(), key=lambda x: (-len(x[1]), x[0]))
        # sorted_items = sorted(pattern_hm.items(), key=lambda x: (-x[1], x[0]))
        return sorted_items[0][0]
        