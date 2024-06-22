# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.size = 0
        self.head = head
        while head:
            self.size += 1
            head = head.next

    def getRandom(self) -> int:
        count = random.randint(1, self.size)
        node = self.head
        count -= 1
        while count > 0:            
            node = node.next
            count -= 1
        return node.val if node else 0



# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()