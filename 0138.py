class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        
        nodes = {}
       
        head = self.recurse(head, 0, nodes)
        node = head
        
        while True:
            if node.random:
                node.random = nodes[id(node.random)]
            
            if node.next == None:
                break
                
            node = node.next
        
        return head


    def recurse(self, node, i, nodes):
        next_node = None
        if node.next != None:
            next_node = self.recurse(node.next, i+1, nodes)

        new = Node(x=node.val, next=next_node, random=node.random)
        nodes[id(node)] = new
        return new
