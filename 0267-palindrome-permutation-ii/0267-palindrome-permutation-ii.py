class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        def backtrack(path):
            if len(path) == len(s):
                result.append(path[:])
                return
            for ch in count:
                if count[ch] > 0:
                    count[ch] -= 2
                    backtrack(ch + path + ch)
                    count[ch] += 2

        count = Counter(s)        
        odd_char = [ char for char, cnt in count.items() if cnt%2 == 1]
        if len(odd_char) > 1:
            return []
        result = []
        odd_char = odd_char[0] if odd_char else ""
        count[odd_char] -= 1
        backtrack(odd_char)
        return result
        