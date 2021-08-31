# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(node, sub):
            if node == None and sub == None:
                return True
            
            if (node and not sub) or (not node and sub):
                return False
            
            if node.val == sub.val:
                return check(node.left, sub.left) and check(node.right, sub.right)
            
            return False
        
        def traverse(node):
            if check(node, subRoot):
                return True
                
            left = traverse(node.left) if node.left else False                
            right = traverse(node.right) if node.right else False
                
            return left or right
            
        return traverse(root)