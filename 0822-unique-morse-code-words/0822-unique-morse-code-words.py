class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        cnt = 0
        s = set()
        for w in words:
            curr = ''
            for c in w:
                idx = ord(c) - ord('a')
                curr += code[idx]
            if curr not in s:
                s.add(curr)
        return len(s)