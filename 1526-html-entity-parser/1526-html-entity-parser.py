class Solution:
    def entityParser(self, text: str) -> str:
        hm = {'&quot;':'"', '&apos;':"'", '&amp;':'&', '&gt;':'>', '&lt;':'<', '&frasl;':'/'}
        i, n = 0, len(text)
        ans = ''
        while i < n:
            if text[i] == '&':
                found = False
                for k in hm.keys():
                    if text[i:i+len(k)] == k:
                        ans += hm[k]
                        i += len(k)
                        found = True
                        break
                if found: continue
            ans += text[i]
            i += 1
        return ans