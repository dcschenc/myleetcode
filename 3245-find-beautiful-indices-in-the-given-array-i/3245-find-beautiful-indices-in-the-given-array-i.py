class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> List[int]:
        n = len(s)
        a_idx, b_idx = [], []
        i, a_len, b_len = 0, len(a), len(b)
        while i < n:
            if s[i:i + a_len] == a:
                a_idx.append(i)
            if s[i:i + b_len] == b:
                b_idx.append(i)
            i += 1
        if len(b_idx) == 0: return []
        ans = set()
        n = len(b_idx)
        for i in a_idx:
            left = bisect_left(b_idx, x = i - k)
            right = bisect_right(b_idx, x = i + k)
            if left < right:
                ans.add(i)     
        return sorted(list(ans))