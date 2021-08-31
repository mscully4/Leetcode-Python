class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        elif not l1:
            head = l2
            l2 = l2.next
        elif not l2:
            head = l1
            l1 = l1.next
        elif l1.val <= l2.val:
            head = l1
            l1 = l1.next
        elif l2.val < l1.val:
            head = l2
            l2 = l2.next
        node = head
        while l2 and l1:
            if l2.val <= l1.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        while l1:
            node.next = l1
            l1 = l1.next
            node = node.next
        while l2:
            node.next = l2
            l2 = l2.next
            node = node.next
        return head
