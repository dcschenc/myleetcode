class Solution:
    def containsPattern(self, arr: List[int], m: int, k: int) -> bool:
        # hm = collections.defaultdict(int)
        # for i in range(m, len(arr)+1):
        #     key = tuple(arr[i-m:i])
        #     # print(key, hm)
        #     hm[key] += 1
        #     if hm[key] == k:
        #         return True
        # return False
        
        n = len(arr) 
        for i in range(n - m*k + 1):           
            if arr[i:i+m] * k == arr[i:i+m*k]:
                return True        
        return False

