class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/3100-3199/3184.Count%20Pairs%20That%20Form%20a%20Complete%20Day%20I
        total = 0
        cnt = Counter()
        for h in hours:
            diff = (24 - h % 24) % 24
            if diff in cnt:
                total += cnt[diff]
            cnt[h % 24] += 1
        return total