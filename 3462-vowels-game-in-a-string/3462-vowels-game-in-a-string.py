class Solution:
    def doesAliceWin(self, s: str) -> bool:
        # https://github.com/doocs/leetcode/tree/main/solution/3200-3299/3227.Vowels%20Game%20in%20a%20String
        vowels = set("aeiou")
        return any(c in vowels for c in s) 