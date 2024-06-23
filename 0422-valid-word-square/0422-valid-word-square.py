class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        m, n = len(words), max(len(word) for word in words)
        matrix = [['' for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(len(words[i])):
                matrix[i][j] = words[i][j]
        if m != n:
            return False
            
        for i in range(m):
            for j in range(n):
                if matrix[i][j] != matrix[j][i]:
                    return False
        return True