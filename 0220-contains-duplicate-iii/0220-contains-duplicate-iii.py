from sortedcontainers import SortedSet

class Solution:
    ###### time complexity: O(n * min(n, k)), space complexity: O(min(n, k)) ###########
    ###### k:indexDiff, t: valueDiff #######

    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        def get_bucket_id(num):
            # Ensure that negative numbers are placed in the previous bucket.
            return (num + 1) // (valueDiff + 1)

        if valueDiff < 0: return False

        buckets = {}  # Dictionary to store elements grouped in buckets.
        width = valueDiff + 1  # Bucket width, considering t.
        for i, num in enumerate(nums):
            bucket_id = get_bucket_id(num)
            if bucket_id in buckets:
                return True
            if (bucket_id - 1) in buckets and abs(num - buckets[bucket_id - 1]) < width:
                return True
            if (bucket_id + 1) in buckets and abs(num - buckets[bucket_id + 1]) < width:
                return True
            buckets[bucket_id] = num
            
            if i >= indexDiff:
                # Remove the element that is no longer in the sliding window.
                del buckets[get_bucket_id(nums[i - indexDiff])]

        return False

        s = SortedSet()
        for i, v in enumerate(nums):
            j = s.bisect_left(v - valueDiff)
            if j < len(s) and s[j] <= v + valueDiff:
                return True
            s.add(v)
            if i >= indexDiff:
                s.remove(nums[i - indexDiff])
        return False


# class Node(object):
#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None
#         self.height = 1

# class AVLTree(object):
#     def __init__(self):
#         self.root = None
#         self.size = 0
        
				
#     def height(self, node):
#         if node:
#             return node.height
#         return 0
    
		
#     def setHeight(self, node):
#         if node is None:
#             return 0
#         return 1 + max(self.height(node.left), self.height(node.right))
    
		
#     def rightRotate(self, node):
#         new_root = node.left
#         node.left = node.left.right
#         new_root.right = node
#         node.height = self.setHeight(node)
#         new_root.height = self.setHeight(new_root)
#         return new_root
    
    
#     def leftRotate(self, node):
#         new_root = node.right
#         node.right = node.right.left
#         new_root.left = node
#         node.height = self.setHeight(node)
#         new_root.height = self.setHeight(new_root)
#         return new_root
        
    
#     def insert(self, node, val):
#         if node == self.root:
#             self.size += 1
#         # Returns a Node pointing to updated subtree
#         if node is None:
#             return Node(val)
#         if node.val < val:
#             node.right = self.insert(node.right, val)
#         else:
#             node.left = self.insert(node.left, val)
#         balance = self.height(node.left) - self.height(node.right)
#         if balance > 1:
#             if self.height(node.left.left) > self.height(node.left.right):
#                 node = self.rightRotate(node)
#             else:
#                 node.left = self.leftRotate(node.left)
#                 node = self.rightRotate(node)
#         elif balance < -1:
#             if self.height(node.right.right) > self.height(node.right.left):
#                 node = self.leftRotate(node)
#             else:
#                 node.right = self.rightRotate(node.right)
#                 node = self.leftRotate(node)
#         else:
#             node.height = self.setHeight(node)
#         return node
    
    
#     def getMinValNode(self, node):
#         if node is None or node.left is None:
#             return node
#         return self.getMinValNode(node.left)
    
		
#     def remove(self, node, val):
#         if node is None:
#             return None
#         if node.val < val:
#             node.right = self.remove(node.right, val)
#         elif node.val > val:
#             node.left = self.remove(node.left, val)
#         else:
#             if node.left is None:
#                 return node.right
#             elif node.right is None:
#                 return node.left
#             else:
#                 right_min_val_node = self.getMinValNode(node.right)
#                 node.val = right_min_val_node.val
#                 node.right = self.remove(node.right, right_min_val_node.val)
        
#         node.height = self.setHeight(node)
#         balance = self.height(node.left) - self.height(node.right)
#         if balance > 1:
#             if self.height(node.left.left) > self.height(node.left.right):
#                 node = self.rightRotate(node)
#             else:
#                 node.left = self.leftRotate(node.left)
#                 node = self.rightRotate(node)
#         elif balance < -1:
#             if self.height(node.right.right) > self.height(node.right.left):
#                 node = self.leftRotate(node)
#             else:
#                 node.right = self.rightRotate(node.right)
#                 node = self.leftRotate(node)
#         else:
#             node.height = self.setHeight(node)
#         return node
    
    
#     def predecessor(self, node, val):
#         if node is None:
#             return None
#         if node.val == val:
#             return val
#         elif node.val > val:
#             return self.predecessor(node.left, val)
#         else:
#             right_res = self.predecessor(node.right, val)
#             return right_res if right_res else node.val    
            
						
#     def successor(self, node, val):
#         if node is None:
#             return None
#         if node.val == val:
#             return val
#         elif node.val < val:
#             return self.successor(node.right, val)
#         else:
#             left_res = self.successor(node.left, val)
#             return left_res if left_res else node.val
    

# class Solution(object):
#     def containsNearbyAlmostDuplicate(self, nums, k, t):
#         """
#         :type nums: List[int]
#         :type k: int
#         :type t: int
#         :rtype: bool
#         """
#         avltree = AVLTree()
#         root = avltree.root
#         for i, num in enumerate(nums):            
#             predecessor = avltree.predecessor(root, num)
#             if predecessor is not None and abs(predecessor - num) <= t:
#                 return True
#             successor = avltree.successor(root, num)
#             if successor is not None and abs(successor - num) <= t:
#                 return True
                        
#             root = avltree.insert(root, num)
            
#             if avltree.size > k:
#                 root = avltree.remove(root, nums[i-k])
                
#         return False


       