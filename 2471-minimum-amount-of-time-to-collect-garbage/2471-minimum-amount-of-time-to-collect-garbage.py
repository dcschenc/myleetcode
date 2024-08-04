class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2300-2399/2391.Minimum%20Amount%20of%20Time%20to%20Collect%20Garbage
        ans = 0
        last = {}
        for i, s in enumerate(garbage):
            ans += len(s)
            for c in s:
                last[c] = i
        s = list(accumulate(travel, initial=0))
        ans += sum(s[i] for i in last.values())
        return ans