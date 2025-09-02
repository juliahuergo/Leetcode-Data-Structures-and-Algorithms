class Solution(object):
    def closestValue(self, root, target):
        if not root:
            return 0
        
        self.ans = root.val 
        
        def aux(root, target, diff):
            if not root:
                return
            
            if abs(root.val-target) == diff:
                self.ans = min(self.ans, root.val)
            
            if abs(root.val-target) < diff:
                self.ans = root.val
                diff = abs(root.val-target)
                
            if root.val > target:
                aux(root.left, target, diff)
                
            else:
                aux(root.right, target, diff)
        
        aux(root, target, float('inf'))
        return self.ans
