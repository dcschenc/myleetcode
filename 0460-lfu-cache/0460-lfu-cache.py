# class Node:
#     def __init__(self, key: int, value: int) -> None:
#         self.key = key
#         self.value = value
#         self.freq = 1
#         self.prev = None
#         self.next = None

# class DoublyLinkedList:
#     def __init__(self) -> None:
#         self.head = Node(-1, -1)
#         self.tail = Node(-1, -1)
#         self.head.next = self.tail
#         self.tail.prev = self.head

#     def add_first(self, node: Node) -> None:
#         node.prev = self.head
#         node.next = self.head.next
#         self.head.next.prev = node
#         self.head.next = node

#     def remove(self, node: Node) -> Node:
#         node.next.prev = node.prev
#         node.prev.next = node.next
#         node.next, node.prev = None, None
#         return node

#     def remove_last(self) -> Node:
#         return self.remove(self.tail.prev)

#     def is_empty(self) -> bool:
#         return self.head.next == self.tail


class LFUCache:
    # https://github.com/doocs/leetcode/tree/main/solution/0400-0499/0460.LFU%20Cache
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.min_freq = 0
        self.key_to_val = {}
        self.key_to_freq = {}
        self.freq_to_keys = defaultdict(OrderedDict)

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1

        # Get the value and the current frequency
        value = self.key_to_val[key]
        freq = self.key_to_freq[key]

        # Remove the key from the current frequency list
        del self.freq_to_keys[freq][key]

        # If the current min frequency list is empty, update the min frequency
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if freq == self.min_freq:
                self.min_freq += 1

        # Update the key's frequency
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = value

        return value

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return

        if key in self.key_to_val:
            # Update the value
            self.key_to_val[key] = value
            # Use the get function to update the frequency of the key
            self.get(key)
            return

        if len(self.key_to_val) >= self.capacity:
            # Evict the least frequently used key
            evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[evict_key]
            del self.key_to_freq[evict_key]

        # Add the new key-value pair
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = value
        self.min_freq = 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)