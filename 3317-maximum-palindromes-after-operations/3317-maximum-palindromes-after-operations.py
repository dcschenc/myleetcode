class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        n = len(words)
        v = Counter(''.join(words)).most_common()     
        pairs = sum([f//2 for _, f in v])        
        sizes = [len(w) for w in words]
        sizes.sort()        
        ans = 0
        for i in range(n):
            need = sizes[i]//2
            if need <= pairs:
                pairs -= need
                ans += 1
            else:
                break        
        return ans