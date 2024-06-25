class Solution:    
    def reverseWords(self, s: str) -> str:        
        return ' '.join([t[::-1] for t in s.split(' ')])        
        
        def reverse_word(word, left, right):
            while left < right:
                word[right], word[left] = word[left], word[right]
                left += 1
                right -= 1

        i,j,length = 0, 0, len(s)        
        sl = list(s)
        sl.append(' ')
        length = len(sl)
        for j in range(length):
            if sl[j] == ' ':         
                reverse_word(sl, i,j-1)
                i = j+1
            j += 1
        return "".join(sl).strip()

    