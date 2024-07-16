class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split()
        words[0] = words[0].lower()
        words.sort(key=len)
        words[0] = words[0].title()
        return " ".join(words)
        
        words = text.split(' ')
        hm = defaultdict(list)
        for i, word in enumerate(words):
            hm[len(word)].append(word.lower())
        ans = []
        for _, v in sorted(hm.items()):
            ans.extend(v)
        ans =  ' '.join(ans)
        ans = ans[0].upper() + ans[1:]
        return ans

