# class LRUCache:
#     def __init__(self, capacity: int):
#         self.capacity = capacity
#         self.cached = {}
#         self.visited = collections.deque()

#     def get(self, key: int) -> int:
#         if key in self.visited:
#             self.visited.remove(key)
#             self.visited.append(key)
#             return self.cached[key]
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.visited:
#             self.visited.remove(key)      
#         if self.capacity == len(self.visited):
#             self.visited.popleft()
#         self.visited.append(key)
#         self.cached[key] = value

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {}
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1

        node = self.dic[key]
        self.remove(node)
        self.add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            old_node = self.dic[key]
            self.remove(old_node)

        node = ListNode(key, value)
        self.dic[key] = node
        self.add(node)

        if len(self.dic) > self.capacity:
            node_to_delete = self.head.next
            self.remove(node_to_delete)
            del self.dic[node_to_delete.key]

    def add(self, node):
        previous_end = self.tail.prev
        previous_end.next = node
        node.prev = previous_end
        node.next = self.tail
        self.tail.prev = node

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev


# class Node:
#     def __init__(self, key, val):
#         self.key, self.val = key, val
#         self.prev = self.next = None

# ### use double linked list ###
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.cap = capacity
#         self.cache = {}  # map key to node
#         self.left, self.right = Node(0, 0), Node(0, 0)
#         self.left.next, self.right.prev = self.right, self.left

#     # remove node from list
#     def remove(self, node):
#         prev, nxt = node.prev, node.next
#         prev.next, nxt.prev = nxt, prev

#     # insert node at right
#     def insert(self, node):
#         prev, nxt = self.right.prev, self.right
#         prev.next = nxt.prev = node
#         node.next, node.prev = nxt, prev

#     def get(self, key: int) -> int:
#         if key in self.cache:
#             self.remove(self.cache[key])
#             self.insert(self.cache[key])
#             return self.cache[key].val
#         return -1

#     def put(self, key: int, value: int) -> None:
#         if key in self.cache:
#             self.remove(self.cache[key])
#         self.cache[key] = Node(key, value)
#         self.insert(self.cache[key])

#         if len(self.cache) > self.cap:
#             # remove from the list and delete the LRU from hashmap
#             lru = self.left.next
#             self.remove(lru)
#             del self.cache[lru.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)