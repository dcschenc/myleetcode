class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        ans = [None] * len(words)
        for word in words:
            idx = int(word[-1]) - 1
            ans[idx] = word[:-1]
        return ' '.join(ans)

        # i, n = 0, len(s)
        # arr = s.split(' ')
        # words = [''] * len(arr)
        # for w in arr:
        #     i = 0
        #     while i < len(w):
        #         if w[i].isdigit():
        #             break
        #         i += 1
        #     idx = int(w[i:]) - 1
        #     words[idx] = w[:i]
        # return ' '.join(words)
                
