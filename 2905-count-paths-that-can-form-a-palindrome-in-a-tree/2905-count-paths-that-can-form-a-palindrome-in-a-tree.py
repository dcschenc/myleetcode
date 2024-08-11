from collections import defaultdict, Counter
class Solution:
    def countPalindromePaths(self, parents: List[int], characters: str) -> int:
        # Helper function to perform Depth-First Search (DFS)
        def dfs(node_index: int, xor_value: int):
            # Accessing the variable 'answer' from the outer scope
            nonlocal answer
            for child_index, char_value in adjacency_list[node_index]:
                # Computing the XOR of the current path's characters
                new_xor = xor_value ^ char_value
                # If the XOR matches any of our previous XOR values, it's a palindrome path
                answer += xor_count[new_xor]
                # Check if toggling any single bit (corresponding to changing one character)
                # results in a palindrome path
                for k in range(26):
                    answer += xor_count[new_xor ^ (1 << k)]
                # Count the occurrences of this XOR value along the path
                xor_count[new_xor] += 1
                # Recursive DFS call to continue the search
                dfs(child_index, new_xor)

        # Size of the tree (number of nodes)
        n = len(parents)
        # Adjacency list to represent the tree and store (child_index, binary representation of the character)
        adjacency_list = defaultdict(list)
        for i in range(1, n):
            parent_index = parents[i]
            adjacency_list[parent_index].append((i, 1 << (ord(characters[i]) - ord('a'))))
      
        # The answer to keep track of the number of palindrome paths
        answer = 0
        # Counter to store the number of times an XOR value has been seen on a path
        xor_count = Counter({0: 1})      
        # Start DFS from the root node with XOR value 0 (since no characters have been visited yet)
        dfs(0, 0)      
        # Return the final count of palindrome paths
        return answer

# from collections import defaultdict, Counter
# class Solution:
#     def countPalindromePaths(self, parent: List[int], s: str) -> int:
#         def dfs(i: int, xor: int):
#             nonlocal ans
#             for j, v in g[i]:
#                 x = xor ^ v
#                 ans += cnt[x]
#                 for k in range(26):
#                     ans += cnt[x ^ (1 << k)]
#                 cnt[x] += 1
#                 dfs(j, x)

#         n = len(parent)
#         g = defaultdict(list)
#         for i in range(1, n):
#             p = parent[i]
#             # bitmask  a: 00000, b: 00010, c 00100
#             g[p].append((i, 1 << (ord(s[i]) - ord('a'))))  
#         ans = 0
#         cnt = Counter({0: 1})
#         dfs(0, 0)
#         return ans