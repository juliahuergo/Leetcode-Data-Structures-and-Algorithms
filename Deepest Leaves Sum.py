class Solution(object):
    def deepestLeavesSum(self, root):
        queue = deque([root])
        
        while queue: #iteration at each level
            ans = 0
            num_nodes_curr_level = len(queue)
            
            for _ in range(num_nodes_curr_level): #iteration at each node of a level
                node = queue.popleft()
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                else:
                    ans += node.val
            if not queue:
                return ans
        
