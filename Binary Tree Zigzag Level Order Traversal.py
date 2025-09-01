class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        
        queue = deque([root])
        ans = []
        RtoL = False
        
        
        while queue: #repeats for every level
            num_nodes_curr_level = len(queue)
            level = []
            
            for _ in range(num_nodes_curr_level): #repeats for every node in a level
                node = queue.popleft()
                
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

                
            if RtoL:
                level.reverse()
                ans.append(level)
            else:
                ans.append(level)
            
            RtoL = not RtoL
        
        return ans
            
            
