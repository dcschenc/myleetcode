class Solution:
    def countValidWords(self, sentence: str) -> int:
        count = 0
        for i, word in enumerate(sentence.split()):
            valid = True
            hyphen_count = 0  
            for j, c in enumerate(word):
                if c.isdigit():
                    valid = False 
                    break
                if c in '!,.' and j != len(word)-1:
                    valid = False 
                    break
                if (c == "-" and (j == len(word)-1 or j == 0)) or (c == "-" and (not word[j-1].isalpha() or not word[j+1].isalpha())):
                    valid = False 
                    break
                if c == "-":
                    hyphen_count += 1
                    if hyphen_count > 1:
                        valid = False 
                        break
            if valid:
                count += 1
        return count
