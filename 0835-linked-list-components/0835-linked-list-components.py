# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:

        # Convert G to a set for faster lookup
        G_set = set(nums)
        
        current = head
        count = 0

        while current:
            # Check if the current node is in the set G
            if current.val in G_set:
                # Increment the count and skip all nodes in the connected component
                count += 1
                while current and current.val in G_set:
                    current = current.next
            else:
                # Move to the next node
                current = current.next

        return count

        nums = set(nums)
        cur = head        
        prev = cur
        count = 0
        start = True
        while cur:
            if cur.val in nums:
                if start:
                    count += 1
                    start = False
            else:
                start = True
            
            if cur.val in nums:
                nums.remove(cur.val)
            cur = cur.next
        return count

