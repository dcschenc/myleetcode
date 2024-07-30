class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        def isPalindroic(w):
            left, right = 0, len(w) - 1
            while left < right:
                if w[left] != w[right]:
                    return False
                left += 1
                right -= 1
            return True

        for w in words:
            if isPalindroic(w):
                return w
        return ''