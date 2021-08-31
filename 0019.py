# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        
        node = head

        nodes = [node]
        while node.next:
            node = node.next
            nodes.append(node)
            
        n = len(nodes) - n
        
        if n == 0:
            return head.next
        
        nodes[n-1].next = nodes[n+1] if n+1 < len(nodes) else None
            
        return head
            