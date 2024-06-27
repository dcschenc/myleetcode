class Node():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        

class MyHashMap(object):

    def __init__(self):
        self.capacity = 1000
        self.hash_table = [None]* self.capacity
    
    def hash(self, key):
        index = key % self.capacity 
        return index    
        
    # This method helps to add a new key, value pair into the hastable
    def put(self, key, value):
        index = self.hash(key)
        
        if self.hash_table[index] == None:
            self.hash_table[index] = Node(key, value)            
        # If the key present in the index, then    
        else:
            curr_node = self.hash_table[index]
            while curr_node:
                if curr_node.key == key:
                    curr_node.value = value
                    return 
                if curr_node.next == None: 
                    break
                curr_node = curr_node.next 
                
            # add the new node to curr .next node.
            curr_node.next = Node(key, value)
        

    def get(self, key):
        index = self.hash(key)
        
        # curr_node is the index of the hashtable
        curr_node =self.hash_table[index]
        
        # Till there is curr_node
        while curr_node:
            
            if curr_node.key == key:
                return curr_node.value
            else:
                curr_node= curr_node.next
        
        # If there is no key present in the hashtable as requested, return -1.
        return -1
        

    def remove(self, key):
        index = self.hash(key)        
        if self.hash_table[index]== None:
            return
        
        curr_node = prev_node = self.hash_table[index]
        
        if curr_node.key == key:
            self.hash_table[index] = curr_node.next
        else:
            
            # Update the curr_ node to next
            curr_node = curr_node.next
            
            while curr_node:
                
                if curr_node.key == key:
                    prev_node.next = curr_node.next
                    break                
                else:
                    prev_node = prev_node.next
                    curr_node = curr_node.next
  



# class MyHashMap:

#     def __init__(self):
#         self.num_buckets = 10
#         self.buckets = [{} for _ in range(self.num_buckets)]
        
#     def get_hash_val(self, key):
#         return key%self.num_buckets

#     def put(self, key: int, value: int) -> None:
#         h_val = self.get_hash_val(key)
#         self.buckets[h_val][key] = value

#     def get(self, key: int) -> int:
#         h_val = self.get_hash_val(key)
#         if key in self.buckets[h_val]:
#             return self.buckets[h_val][key]
#         else:
#             return -1

#     def remove(self, key: int) -> None:
#         h_val = self.get_hash_val(key)
#         if key in self.buckets[h_val]:
#             del self.buckets[h_val][key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)