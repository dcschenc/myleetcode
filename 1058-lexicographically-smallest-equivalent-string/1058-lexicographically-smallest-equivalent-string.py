from collections import defaultdict, deque
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:    
        # https://algo.monster/liteproblems/1061

        base_str = baseStr
        # Initialize the parent array for union-find structure to point
        # each element to itself.
        parent = list(range(26))
      
        # The find function uses path compression for finding the
        # representative of a set.
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        # Merge the sets of characters in strings s1 and s2
        for i in range(len(s1)):
            char_s1, char_s2 = ord(s1[i]) - ord('a'), ord(s2[i]) - ord('a')
            parent_s1, parent_s2 = find(char_s1), find(char_s2)
            # Link the sets by rank (in this case, by smallest representative).
            if parent_s1 < parent_s2:
                parent[parent_s2] = parent_s1
            else:
                parent[parent_s1] = parent_s2

        # Build the resulting equivalent string based on the base string
        # by replacing each character with its smallest equivalent.
        result = []
        for char in base_str:
            char_index = ord(char) - ord('a')
            result.append(chr(find(char_index) + ord('a')))
      
        # Join and return the computed characters as a single string.
        return ''.join(result)


        # adj = defaultdict(list)
        # for c1, c2 in zip(s1, s2):
        #     adj[c1].append(c2)
        #     adj[c2].append(c1)
        # flag = [False] * 26
        # mapping = []
        # for u, v in adj.items():
        #     if flag[ord(u) - ord('a')]:
        #         continue
        #     flag[ord(u) - ord('a')] = True
        #     queue = deque()
        #     queue.append(u)
        #     visited = set()
        #     while queue:
        #         for _ in range(len(queue)):
        #             i = queue.popleft()
        #             if i in visited:
        #                 continue
        #             visited.add(i)
        #             for n in adj[i]:
        #                 queue.append(n)
        #     for i in visited:
        #         flag[ord(i) - ord('a')] = True
        #     mapping.append(list(visited))        

        # for v in mapping:
        #     v.sort()
       
        # # print(mapping)
        # ans = ''
        # for c in baseStr:
        #     found = False
        #     for group in mapping:
        #         if c in group:
        #             ans += group[0]
        #             found = True
        #             break
        #     if found is False:
        #         ans += c
        # return ans


        # mapping = []
        # # hm = defaultdict(list)
        # for c1, c2 in zip(s1, s2):
        #     found = False
        #     print(mapping)
        #     for v in mapping:
        #         if c1 in v:
        #             v.append(c2)
        #             found = True                    
        #         elif c2 in v:
        #             v.append(c1)
        #             found = True
        #         if found:
        #             break
        #     if found is False:
        #         mapping.append([c1, c2])

        # for v in mapping:
        #     v.sort()
       
        # print(mapping)
        # ans = ''
        # for c in baseStr:
        #     found = False
        #     for group in mapping:
        #         if c in group:
        #             ans += group[0]
        #             found = True
        #             break
        #     if found is False:
        #         ans += c
        # return ans