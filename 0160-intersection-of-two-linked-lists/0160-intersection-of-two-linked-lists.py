# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes_in_B = set()

        while headB is not None:
            nodes_in_B.add(headB)
            headB = headB.next

        while headA is not None:
            # if we find the node pointed to by headA,
            # in our set containing nodes of B, then return the node
            if headA in nodes_in_B:
                return headA
            headA = headA.next

        return None
        
        # visited_1 = {}
        # visited_2 = {}
        # node_1, node_2 = headA, headB
        # len_1 = 0
        # while node_1:
        #     len_1 += 1
        #     node_1 = node_1.next
        # len_2 = 0
        # while node_2:
        #     len_2 += 1
        #     node_2 = node_2.next

        # node_1, node_2 = headA, headB
        # if len_1 < len_2:
        #     while len_1 != len_2:
        #         node_2 = node_2.next
        #         len_2-= 1
        # else:
        #     while len_1 != len_2:
        #         node_1 = node_1.next
        #         len_1 -= 1
                
        # while node_1:
        #     if node_1 == node_2:
        #         return node_1
        #     else:
        #         node_1 = node_1.next
        #         node_2 = node_2.next
        # return None

        
        
        # while node_1 or node_2:
        #     # print(node_1.val, node_2.val)
        #     if node_1 in visited_2:
        #         return node_1
        #     visited_1[node_1] = node_1
        #     if node_1:
        #         node_1 = node_1.next
                
        #     if node_2 in visited_1:
        #         return node_2
        #     visited_2[node_2] = node_2
        #     if node_2:
        #         node_2 = node_2.next
        # return None
        