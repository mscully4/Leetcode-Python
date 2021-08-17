class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        # global target_count
        target_count = 0
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
                nonlocal target_count
                target_count += 1
                
        traverse(root, s)
        return bool(target_count)