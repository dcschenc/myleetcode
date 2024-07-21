class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/1600-1699/1601.Maximum%20Number%20of%20Achievable%20Transfer%20Requests
        def check(mask: int) -> bool:
            cnt = [0] * n
            for i, (f, t) in enumerate(requests):
                if mask >> i & 1:
                    cnt[f] -= 1
                    cnt[t] += 1
            return all(v == 0 for v in cnt)

        ans = 0
        for mask in range(1 << len(requests)):
            cnt = mask.bit_count()
            if ans < cnt and check(mask):
                ans = cnt
        return ans
