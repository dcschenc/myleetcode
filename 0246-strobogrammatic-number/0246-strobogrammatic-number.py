class Solution:
    def isStrobogrammatic(self, num: str) -> bool:        
        hm = {'9': '6', '8':'8', '0':'0', '6':'9', '1':'1'}
        n = len(num)
        i, j = 0, n-1
        while i < j:
            if num[i] in hm and hm[num[i]] == num[j]:
                i += 1
                j -= 1
            else:
                return False
        if i == j and num[i] not in ['8', '0', '1']:
            return False
        return True