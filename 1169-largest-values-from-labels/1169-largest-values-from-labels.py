class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], numWanted: int, useLimit: int) -> int:
        # res = []
        # count = 0
        # hm = {}
        # for i in range(len(values)):
        #     if len(res) >= numWanted:
        #         break
        #     count = hm.get(labels[i], 0)
        #     if count < useLimit:
        #         res.append(values[i])
        #         hm[labels[i]] = 1 + hm.get(labels[i],0)
        # return sum(res)
        pairs = []
        for i in range(len(values)):
            pairs.append((values[i], labels[i]))
        pairs.sort(key=lambda x:x[0], reverse=True)
        hm = {}
        res = 0
        count = 0
        # print(pairs)
        for val, label in pairs:
            if count >= numWanted:
                break
            if hm.get(label,0) < useLimit:
                res += val
                hm[label] = 1 + hm.get(label, 0)
                count += 1
        return res