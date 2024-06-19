# https://github.com/doocs/leetcode/tree/main/solution/0200-0299/0212.Word%20Search%20II

class Trie:
    def __init__(self):
        self.children: List[Trie | None] = [None] * 26
        self.ref: int = -1

    def insert(self, w: str, ref: int):
        node = self
        for c in w:
            idx = ord(c) - ord('a')
            if node.children[idx] is None:
                node.children[idx] = Trie()
            node = node.children[idx]
        node.ref = ref

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node: Trie, i: int, j: int):
            idx = ord(board[i][j]) - ord('a')
            if node.children[idx] is None:
                return
            node = node.children[idx]
            if node.ref >= 0:
                ans.append(words[node.ref])
                node.ref = -1
            c = board[i][j]
            board[i][j] = '#'
            for a, b in pairwise((-1, 0, 1, 0, -1)):
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and board[x][y] != '#':
                    dfs(node, x, y)
            board[i][j] = c

        tree = Trie()
        for i, w in enumerate(words):
            tree.insert(w, i)
        m, n = len(board), len(board[0])
        ans = []
        for i in range(m):
            for j in range(n):
                dfs(tree, i, j)
        return ans

# class Trie:
#     def __init__(self):
#         # Initializing the children with an array of 26 Trie nodes representing each character of the alphabet.
#         self.children: List[Trie | None] = [None] * 26
#         # Reference to the index of the word in the words list, -1 if it's not a complete word.
#         self.ref: int = -1

#     def insert(self, word: str, ref: int):
#         node = self
#         # Insert each character of the word in the Trie.
#         for char in word:
#             index = ord(char) - ord('a')
#             # If the child node for this character does not exist, create it.
#             if node.children[index] is None:
#                 node.children[index] = Trie()
#             node = node.children[index]
#         # Set the reference index for the last character node to the word's index in the input list.
#         node.ref = ref


# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         def dfs(node: Trie, i: int, j: int):
#             # Conducts a depth-first search starting from board[i][j].
#             index = ord(board[i][j]) - ord('a')
#             # If there's no child node for this character, return.
#             if node.children[index] is None:
#                 return
#             node = node.children[index]
#             # If this node is a complete word, add to the answer list and mark it as visited.
#             if node.ref >= 0:
#                 ans.append(words[node.ref])
#                 node.ref = -1
#             # Temporarily mark the board position as visited by replacing the character with '#'.
#             temp_char = board[i][j]
#             board[i][j] = '#'
#             # Visit all neighbors (up, right, down, left).
#             for x_offset, y_offset in zip(*[iter([-1, 0, 1, 0, -1])] * 2):
#                 x, y = i + x_offset, j + y_offset
#                 # If the new position is within bounds and not visited, continue DFS.
#                 if 0 <= x < m and 0 <= y < n and board[x][y] != '#':
#                     dfs(node, x, y)
#             # Restore the original character after visiting neighbors.
#             board[i][j] = temp_char

#         # Initialize the Trie and fill it with the words.
#         trie_root = Trie()
#         for index, word in enumerate(words):
#             trie_root.insert(word, index)
#         # Get the dimensions of the board.
#         m, n = len(board), len(board[0])
#         # List to store the answer words.
#         ans = []
#         # Loop through each cell in the board and start DFS if possible.
#         for i in range(m):
#             for j in range(n):
#                 dfs(trie_root, i, j)
#         return ans




# class Solution:
#     def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
#         def backtrack(i, j, w):
#             if w in words and w not in res:
#                 res.add(w)
#             if len(w) >= max_len:
#                 return
#             for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
#                 x, y = dx + i, dy + j
#                 if 0 <= x <= m-1 and 0 <= y <= n-1 and visited[x][y] is False:
#                     visited[x][y] = True
#                     backtrack(x, y, w + board[x][y])
#                     visited[x][y] = False

#         words = set(words)
#         max_len = max([len(word) for word in words])
#         m, n = len(board), len(board[0])
#         res = set()
#         for i in range(m):
#             for j in range(n):
#                 visited = [[False for j in range(n)] for i in range(m)]
#                 visited[i][j] = True
#                 backtrack(i, j, board[i][j])
#         return list(res)