class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter(s)
        for i, c in enumerate(s):
            if cnt[c] == 1:
                return i
        return -1
        
        dict_ = {}
        for c in s:
            if c in dict_:
                dict_[c] += 1
            else:
                dict_[c] = 1
        for i in dict_:
            if dict_[i] == 1:
                return s.index(i)
        # for i, c in enumerate(s):
        #     if dict_[c] == 1:
        #         return i
        return -1
                