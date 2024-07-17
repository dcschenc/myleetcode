class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        kv = sorted(counter.items(), key=lambda x: x[1])
        for key, val in kv:
            if val <= k:
                counter[key] = 0
                k -= val
            else:
                break
        return len([k for k, v in counter.items() if v > 0])

