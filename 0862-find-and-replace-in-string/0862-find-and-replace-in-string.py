class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = ''
        pre_idx = 0
        for idx, src, tar in sorted(zip(indices, sources, targets), key=lambda x: x[0]):            
            ans += s[pre_idx:idx]
            if s[idx:].startswith(src):
                ans += tar
                pre_idx = idx + len(src)
            else:
                pre_idx = max(pre_idx, idx)
        if pre_idx < len(s):
            ans += s[pre_idx:]
        return ans