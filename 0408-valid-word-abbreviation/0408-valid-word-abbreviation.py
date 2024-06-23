class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0    
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == "0":
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
            elif word[i] != abbr[j]:
                return False
            else:
                i += 1
                j += 1

        return i == len(word) and j == len(abbr)

        # n, m = len(word), len(abbr)
        # i, j = 0, 0

        # while j < m:
        #     if i > n - 1:
        #         return False
        #     if not abbr[j].isdigit():
        #         if word[i] != abbr[j]:
        #             return False
        #         i += 1
        #         j += 1
        #         continue
        #     if abbr[j] == '0':
        #         return False
        #     start = j
        #     j += 1
        #     while j < m and abbr[j].isdigit():
        #         j+=1
        #     num = int(abbr[start:j])
        #     i = i + num
        #     if i > n:
        #         return False            
        # if i <= n-1:
        #     return False
        # return True
