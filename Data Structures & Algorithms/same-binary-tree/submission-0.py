# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        Base Cases: 1. Both null (T), 2. Diff (F), 3. Same so check children (DFS)
        '''

        if not p and not q: #Both null
            return True
        
        if not p or not q or p.val != q.val: #Checks if 1 null and if both exist but !=
            return False #Grouped together since null value raises attribute exception error!

        return self.isSameTree(q.left, p.left) and self.isSameTree(q.right, p.right)
        

         