class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        # https://github.com/doocs/leetcode/tree/main/solution/2500-2599/2516.Take%20K%20of%20Each%20Character%20From%20Left%20and%20Right
        cnt = Counter(s)
        if any(cnt[c] < k for c in "abc"):
            return -1
        mx = left = 0
        for right, c in enumerate(s):
            cnt[c] -= 1
            while cnt[c] < k:
                cnt[s[left]] += 1
                left += 1
            mx = max(mx, right - left + 1)
        return len(s) - mx