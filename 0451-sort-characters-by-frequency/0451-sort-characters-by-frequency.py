
from collections import defaultdict
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        # hm = defaultdict(int)
        # for c in s:
        #     hm[c] += 1
        sorted_dict = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        # print(sorted_dict)
        result = ''
        for k, v in sorted_dict:
            result += k*v
        return result