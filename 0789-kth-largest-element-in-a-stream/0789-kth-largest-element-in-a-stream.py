class TreeNode:
    def __init__(self, val):
        self.val = val
        self.count = 1
        self.right = None
        self.left = None
        
import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # self.root = self._init_tree(nums)
        # self.k = k
        self.k = k
        self.min_heap = []

        # Initialize the heap with the first k elements
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:        
        # self._insert_node(val)        
        # return self._find_kth_largest()

        # Add the new element to the heap
        heapq.heappush(self.min_heap, val)

        # If the size of the heap exceeds k, remove the smallest element
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

        # The kth largest element is now the smallest element in the heap
        return self.min_heap[0]
    
    def _find_kth_largest(self):
        """
        In other word, for each node in a BST, 
        if m nodes in the right subtree, the node itself is the m + 1 largest element in the existed array.
        """
        k = self.k
        
        node = self.root
        
        while node:
            
            right_count = 0
            left_count = 0
            
            if node.right:
                right_count = node.right.count
                
            if node.left:
                left_count = node.left.count
                
            if node.count - left_count >= k and k > right_count: 
                return node.val
            
            elif right_count >= k: 
                # return f(node.right, k)
                node = node.right
            else:           
                # return f(node.left, k - (node.count - left_count))
                k = k - (node.count - left_count)
                node = node.left
 
                        
    
    def _init_tree(self, nums):
        
        if not nums:
            return None
        
        root_val = nums.pop()
        self.root = TreeNode(root_val)
        
        for num in nums:
            self._insert_node(num)
        
        return self.root
        
    def _insert_node(self, val):
        new_node = TreeNode(val)

        if not self.root:
            self.root = new_node
            return new_node
        
        node = self.root
        
        while node:
            
            node.count += 1
 
            if node.val < val:
                # go right
                if node.right:
                    node = node.right
                else:
                    node.right = new_node
                    break
            else:
                # go left
                if node.left:
                    node = node.left
                else:
                    node.left = new_node
                    break
            


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)




# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):
#         self.nums = sorted(nums)
#         self.k = k

#     def add(self, val: int) -> int:
#         index = self.findIndex(val,0,len(self.nums)-1)
#         self.nums.insert(index,val)
#         return self.nums[-self.k]
    
#     def findIndex(self,val,low,high) -> int:
#         if low > high:
#             return low
#         pivot = (low+high)//2
#         if self.nums[pivot] == val:
#             return pivot
#         if val < self.nums[pivot]:
#             return self.findIndex(val,low,pivot-1)
#         if val > self.nums[pivot]:
#             return self.findIndex(val,pivot+1,high)
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)