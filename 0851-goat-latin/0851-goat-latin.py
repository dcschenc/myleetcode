class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words = sentence.split()
        for i in range(len(words)):
            if words[i][0].lower() not in 'aeiou':                
                words[i] = words[i][1:] + words[i][0]
            words[i] = words[i] + 'ma'
            words[i] = words[i] + 'a'*(i+1)
        return ' '.join(words)