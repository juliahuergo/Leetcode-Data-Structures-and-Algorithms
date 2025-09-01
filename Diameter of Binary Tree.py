class Solution(object):
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        
        self.ans = 0
        
        def aux(root): #adds the two highest depths from a node
            if not root:
                return 0
            left = aux(root.left) 
            right = aux(root.right) 
            
            self.ans = max(self.ans, left+right) 
            return max(left, right) + 1
        
        aux(root)
        return self.ans
