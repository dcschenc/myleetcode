class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        s = set()
        i, n = 0, len(word)
        while i < n:
            if word[i].isdigit():
                while i < n and word[i] == '0':
                    i += 1
                j = i
                while j < n and word[j].isdigit():
                    j += 1
                s.add(word[i:j])
                i = j
            i += 1
        return len(s)

        
        result = set()
        i = 0
        cur = ''
        while i < len(word):
            if word[i].isdigit():
                cur += word[i]
            else:
                if cur != '':
                    result.add(int(cur))
                    cur = ''
            i += 1
        if cur != '':
            result.add(int(cur))
        return len(result)
