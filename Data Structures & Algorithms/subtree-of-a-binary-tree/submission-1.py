# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root: return False
        def isSame(p, q):
            if not p and not q:
                return True
            
            if q and p and q.val == p.val:
                if not isSame(p.left, q.left) or not isSame(p.right, q.right):
                    return False
            else:
                return False
            
            return True
        
        if root.val == subRoot.val and isSame(root, subRoot):
            return True
        
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)