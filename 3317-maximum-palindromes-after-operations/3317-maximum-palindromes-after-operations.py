class Solution:
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        count = Counter(''.join(words))
        odd,even = 0,0
        ans = 0
        
        for val in count.values():
            even += val - val % 2
            odd += val % 2

        words.sort(key=len)

        for word in words:
            length = len(word)            
            evenLenReq = length - (length%2)
            oddLenReq = length %2

            if (even>=evenLenReq and odd>=oddLenReq):
                ans+=1
                even-=evenLenReq
                odd-=oddLenReq   
            elif even>=length:
                ans+=1
                even-=length
               
        return ans