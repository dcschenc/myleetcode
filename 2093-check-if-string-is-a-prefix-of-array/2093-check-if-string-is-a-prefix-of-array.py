class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prestr = ''
        for w in words:
            prestr += w
            if s == prestr:
                return True
        return False