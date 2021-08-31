# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next == None or k == 0:
            return head
        
        runs = 0
        depth = 1
        while runs < k:
            
            node = head
            prev = None

            while True:
                if not node.next:
                    prev.next = None
                    node.next = head
                    break
                else:
                    if runs == 0: depth += 1
                    prev = node
                    node = node.next
                    
            runs += 1
            if k > depth:
                mod = k % depth
                k = depth if mod == 0 else mod
            head = node
                
        return node