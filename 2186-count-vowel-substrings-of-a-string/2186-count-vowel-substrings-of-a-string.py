from collections import defaultdict
class Solution:
    def countVowelSubstrings(self, word: str) -> int:    
        # https://github.com/doocs/leetcode/tree/main/solution/2000-2099/2062.Count%20Vowel%20Substrings%20of%20a%20String
        n = len(word)
        s = set('aeiou')
        return sum(set(word[i:j]) == s for i in range(n) for j in range(i + 1, n + 1))

        n = len(word)
        ans = 0
        for i in range(n):
            if word[i] not in 'aeiou':
                continue
            hm = defaultdict(int)
            hm[word[i]] += 1            
            for j in range(i+1, n):
                if word[j] not in 'aeiou':
                    break
                hm[word[j]] += 1
                found = True
                for c in 'aeiou':
                    if hm[c] < 1:
                        found = False
                        break
                if found:
                    ans += 1
        return ans
