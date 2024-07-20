class Solution:
    def reorderSpaces(self, text: str) -> str:
        total = text.count(' ')
        arr = text.split()
        words = [w for w in arr if w != ' ']        
        if len(words) == 1:
            return words[0] + ' ' * total
        cnt = len(words) 
        space = total//(cnt-1)
        extra = total % (cnt-1)
        ans = words[0]
        for w in words[1:]:
            ans += ' ' * space + w
       
        return ans + ' ' * extra