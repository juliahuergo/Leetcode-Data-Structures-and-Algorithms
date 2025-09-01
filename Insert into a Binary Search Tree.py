class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            #insert here val
            return TreeNode(val)
        
        if root.val > val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)
        
        return root
