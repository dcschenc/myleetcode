class Solution:
    def betterCompression(self, compressed: str) -> str:
        i, n = 0, len(compressed)
        cnt = Counter()
        while i < n:
            c = compressed[i]
            j = i + 1
            while j < n and compressed[j].isdigit():
                j += 1
            cnt[c] += int(compressed[i+1:j])
            i = j
            
        ans = ''
        for c in string.ascii_lowercase:
            if c in cnt:
                ans += c + str(cnt[c])
        return ans
