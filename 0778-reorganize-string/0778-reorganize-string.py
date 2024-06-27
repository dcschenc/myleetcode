from heapq import heappush, heappop
from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:    
        # https://github.com/doocs/leetcode/tree/main/solution/0700-0799/0767.Reorganize%20String
        ## O(n)
        n = len(s)
        cnt = Counter(s)
        mx = max(cnt.values())
        if mx > (n + 1) // 2:
            return ''
        i = 0
        ans = [None] * n
        for k, v in cnt.most_common():
            while v:
                ans[i] = k
                v -= 1
                i += 2
                if i >= n:
                    i = 1
        return ''.join(ans)
        
        ## O(nlogk)
        S = s         
        char_count = Counter(S)
        max_heap = [(-count, char) for char, count in char_count.items()]
        heapq.heapify(max_heap)

        result = []
        while len(max_heap) >= 2:
            count1, char1 = heapq.heappop(max_heap)
            count2, char2 = heapq.heappop(max_heap)

            result.extend([char1, char2])
            if count1 + 1:
                heapq.heappush(max_heap, (count1 + 1, char1))
            if count2 + 1:
                heapq.heappush(max_heap, (count2 + 1, char2))

        if max_heap:
            count, char = heapq.heappop(max_heap)
            if count < -1:
                return ""
            result.append(char)

        return "".join(result)