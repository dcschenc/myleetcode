class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:        
        # https://github.com/doocs/leetcode/tree/main/solution/1000-1099/1090.Largest%20Values%20From%20Labels
        ans = num = 0
        cnt = Counter()
        for v, l in sorted(zip(values, labels), reverse=True):
            if cnt[l] < useLimit:
                cnt[l] += 1
                num += 1
                ans += v
                if num == numWanted:
                    break
        return ans
        
        pairs = []
        for i in range(len(values)):
            pairs.append((values[i], labels[i]))
        pairs.sort(key=lambda x:x[0], reverse=True)
        hm = {}
        res = 0
        count = 0
        for val, label in pairs:
            if count >= numWanted:
                break
            if hm.get(label, 0) < useLimit:
                res += val
                hm[label] = 1 + hm.get(label, 0)
                count += 1
        return res