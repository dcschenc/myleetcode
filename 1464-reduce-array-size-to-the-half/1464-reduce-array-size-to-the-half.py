class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        counter = Counter(arr)
        n = len(arr)
        cnt = 0
        ans = 0
        for k, v in sorted(counter.items(), key = lambda x: x[1], reverse=True):
            cnt += v
            ans += 1
            if cnt >= n//2:
                break
        return ans