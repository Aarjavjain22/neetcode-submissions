# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node,Max):
            if not node:
                return 0
            if node.val>= Max:
                answer=1
            else:
                answer=0
            Max= max(Max,node.val)
            answer+=dfs(node.left, Max)
            answer+=dfs(node.right, Max)
            return answer
        return dfs(root,root.val)