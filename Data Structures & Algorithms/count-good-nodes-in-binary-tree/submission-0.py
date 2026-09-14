# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def dfs(node, max_value):
            nonlocal count

            if not node:
                return
            
            if node.val >= max_value:
                count += 1
            new_max = max(node.val, max_value)
            
            dfs(node.right, new_max)
            dfs(node.left, new_max)
        
        dfs(root, root.val)
        return count
            


        