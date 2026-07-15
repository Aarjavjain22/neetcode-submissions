# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev_val = float('-inf')
              
        def inorder(node):
            nonlocal prev_val            
            if not node:
                return True        
            if not inorder(node.left):
                return False           
            if node.val <= prev_val:
                return False            
            prev_val = node.val
            if not inorder(node.right):
                return False            
            return True
        return inorder(root)
        