class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs(a, b):
            if a == None and b == None:
                return True
            elif (a == None and b != None) or (a != None and b == None):
                return False
            elif a.val == b.val:
                return dfs(a.left, b.left) and dfs(a.right, b.right)
            else:
                return False

        return dfs(p, q)