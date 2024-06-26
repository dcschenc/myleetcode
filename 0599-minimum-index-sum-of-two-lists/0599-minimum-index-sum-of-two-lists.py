class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hm = {}
        res = []
        min_len = 2001
        for i, s in enumerate(list1):
            hm[s] = i
        for j, s in enumerate(list2):
            if s in hm:
                cur = j + hm[s]
                if  cur < min_len:
                    min_len = cur
                    res = [s]
                elif cur == min_len:
                    res.append(s)
        return res