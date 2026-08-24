# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        seen_nodes = set({head})
        while head.next != None:
            node = head.next
            if node not in seen_nodes:
                seen_nodes.add(node)
                head = node
            else:
                return node
        return None
