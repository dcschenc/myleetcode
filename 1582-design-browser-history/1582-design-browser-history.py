# Linked List Implementation
# class ListNode:
#     def __init__(self, val, prev=None, next=None):
#         self.val = val
#         self.prev = prev
#         self.next = next

class BrowserHistory:
    def __init__(self, homepage: str):
        self.current = homepage
        self.back_stack = []
        self.forward_stack = []

    def visit(self, url: str) -> None:
        self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()

    def back(self, steps: int) -> str:
        while steps > 0 and self.back_stack:
            self.forward_stack.append(self.current)
            self.current = self.back_stack.pop()
            steps -= 1
        return self.current

    def forward(self, steps: int) -> str:
        while steps > 0 and self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
            steps -= 1
        return self.current


# Array Implementation
class BrowserHistory:    
    def __init__(self, homepage: str):
        self.i = 0
        self.len = 1
        self.history = [homepage]

    # O(1)
    def visit(self, url: str) -> None:
        if len(self.history) < self.i + 2:
            self.history.append(url)
        else:
            self.history[self.i + 1] = url
        self.i += 1
        self.len = self.i + 1

    # O(1)
    def back(self, steps: int) -> str:
        self.i = max(self.i - steps, 0)
        return self.history[self.i]

    # O(1)
    def forward(self, steps: int) -> str:
        self.i = min(self.i + steps, self.len - 1)
        return self.history[self.i]



# class LinkListNode:
#     def __init__(self, val):
#         self.val = val
#         self.prev = None
#         self.next = None

# class BrowserHistory:

#     def __init__(self, homepage: str):
#         self.left = LinkListNode('')
#         self.right = LinkListNode('')
#         cur = LinkListNode(homepage)        
#         cur.prev = self.left
#         cur.next = self.right
#         self.left.next = cur
#         self.right.prev = cur        
#         self.cur = cur

#     def visit(self, url: str) -> None:
#         visited = LinkListNode(url)
#         visited.prev = self.cur
#         visited.next = self.right
#         self.cur.next = visited       
#         self.right.prev = visited
#         self.cur = visited

#     def back(self, steps: int) -> str:
#         cur = self.cur
#         while cur.prev != self.left and steps > 0:
#             steps -= 1
#             cur = cur.prev
#         # if cur != self.left and steps == 0:
#         self.cur = cur
#         return cur.val

#     def forward(self, steps: int) -> str:
#         cur = self.cur
#         while cur.next != self.right and steps > 0:
#             steps -= 1
#             cur = cur.next
#         # if cur != self.right and steps == 0:
#         self.cur = cur
#         return cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)