class Solution:
    def minDeletions(self, s: str) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1647.Minimum%20Deletions%20to%20Make%20Character%20Frequencies%20Unique
        counter = Counter(s)
        frequencies = set(counter.values())
        sorted_items = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        cnt = 0        
        # print(sorted_items)
        for i in range(1, len(sorted_items)):
            if sorted_items[i][1] == sorted_items[i-1][1]:
                cur = sorted_items[i][1] - 1
                while cur > 0:
                    if cur not in frequencies:
                        frequencies.add(cur)
                        break
                    cur = cur - 1
                # if cur != 0:
                cnt += sorted_items[i][1] - cur
        return cnt

