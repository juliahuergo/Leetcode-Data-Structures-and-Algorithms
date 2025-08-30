class Solution(object):
    def maxAncestorDiff(self, root):
        if not root:
            return 0
        
        self.ans = 0
        def aux(root, maximum, minimum):
            if not root:
                return
            
            self.ans = max(self.ans, abs(root.val-maximum), abs(root.val-minimum))
            
            left = aux(root.left, max(maximum, root.val), min(minimum, root.val))
            right = aux(root.right, max(maximum, root.val), min(minimum, root.val))
        
        aux(root, root.val, root.val)
        return self.ans
