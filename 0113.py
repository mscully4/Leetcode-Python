class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        global results
        results = []
        s = []
        
        def traverse(node, s):
            if node.right:
                s.append(node.val)
                traverse(node.right, s)
                s.pop(-1)
                
            if node.left:
                s.append(node.val)
                traverse(node.left, s)
                s.pop(-1)
                
            if not node.right and not node.left and sum(s) + node.val == targetSum:
                results.append(s + [node.val])
                
        traverse(root, s)
        return results