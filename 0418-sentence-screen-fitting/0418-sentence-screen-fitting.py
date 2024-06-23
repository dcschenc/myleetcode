class Solution:
    def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
        full_sentence = " ".join(sentence) + " "
        length = len(full_sentence)
        start = 0

        for i in range(rows):
            start += cols
            # If the next character is a space, move to the next row
            if full_sentence[start % length] == ' ':
                start += 1
            # If the next character is part of a word, move the start index backward to the beginning of the word
            else:
                while start > 0 and full_sentence[(start - 1) % length] != ' ':
                    start -= 1

        # Calculate how many times the full_sentence can be fitted
        return start // length
        
        i = 0
        cur, cnt = 0, 0
        while i < rows:
            j = 0
            while j < cols:
                if cols - j >= len(sentence[cur]):
                    j += len(sentence[cur]) + 1
                    cur += 1
                    if cur == len(sentence):
                        cnt += 1
                        cur = 0
                else:
                    break
            i += 1
        return cnt
