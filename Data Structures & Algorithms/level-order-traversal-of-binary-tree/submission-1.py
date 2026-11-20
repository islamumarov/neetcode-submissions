# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = [[root.val]]
        def dfs(node, level):
            nonlocal res
            if not node: return
            if len(res)-1 < level:
                res.append([node.val])
            else:
                res[level].append(node.val)
            
            dfs(node.left, level+1)
            dfs(node.right, level+1)
        
        dfs(root.left, 1)
        dfs(root.right, 1)
        return res



