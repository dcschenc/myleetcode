class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hm = Counter(arr)
        for s in arr:
            if hm[s] == 1:
                k -= 1
                if k == 0:
                    return s
        return ""
