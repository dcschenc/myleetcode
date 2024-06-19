"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:    
    def __init__(self):
        self.adj = {}
        
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if node in self.adj:
            return self.adj[node]
        clone = Node(node.val, [])
        self.adj[node] = clone
        for neighbor in node.neighbors:
            clone.neighbors.append(self.cloneGraph(neighbor))
        return clone

    # def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
    #     if node is None:
    #         return None
        
    #     def dfs_nodes(curr):
    #         new_node = Node(curr.val)
    #         node_map[curr] = new_node
    #         for nb in curr.neighbors:
    #             if nb not in visited:                
    #                 visited.add(nb)
    #                 dfs_nodes(nb)
                    
    #     def dfs_nb(curr):
    #         new_node = node_map[curr]       
    #         for nb in curr.neighbors:
    #             new_node.neighbors.append(node_map[nb])
    #             if nb not in visited:                      
    #                 visited.add(nb)
    #                 dfs_nb(nb)
                    
    #     visited = set()            
    #     node_map = {}
    #     visited.add(node)
    #     dfs_nodes(node)

    #     visited.clear()
    #     visited.add(node)
    #     dfs_nb(node)        
    #     return node_map[node]    
        
#     def dfs(self, curr):
#         new_node = Node(curr.val)
#         self.node_map[curr] = new_node
#         for nb in curr.neighbors:
#             if nb not in self.visited:                
#                 self.visited.add(nb)
#                 self.dfs(nb)
                
#     def dfs_add_nb(self, curr):
#         new_node = self.node_map[curr]       
#         for nb in curr.neighbors:
#             new_node.neighbors.append(self.node_map[nb])
#             if nb not in self.visited:                      
#                 self.visited.add(nb)
#                 self.dfs_add_nb(nb)
                
        
                    