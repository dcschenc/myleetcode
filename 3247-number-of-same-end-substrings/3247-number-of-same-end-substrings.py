class Solution:
    def sameEndSubstringCount(self, s: str, queries: List[List[int]]) -> List[int]:
        # https://github.com/doocs/leetcode/tree/main/solution/2900-2999/2955.Number%20of%20Same-End%20Substrings
        hm = defaultdict(list)
        n = len(s)
        for i, c in enumerate(s):
            for char in string.ascii_lowercase:
                if i == 0:
                    hm[char] = [0] * (n + 1)
                else:
                    hm[char][i + 1] = hm[char][i]
            hm[c][i+1] += 1

        ans = []
        for l, r in queries:
            cur = 0
            for c in string.ascii_lowercase:
                cnt = hm[c][r + 1] - hm[c][l]
                cur += cnt * (cnt + 1) // 2
            ans.append(cur)
        return ans