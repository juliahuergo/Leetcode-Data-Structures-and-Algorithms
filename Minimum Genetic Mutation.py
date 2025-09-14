class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        
        def neighbours(node): #generate all mutations of a gene (valid and not valid)
            ans = []
            letters = ['A', 'C', 'G', 'T']
            for i in range(8):
                for letter in letters:
                    mut = node[:i] + letter + node[i+1:]
                    if mut != node:
                        ans.append(mut)
            return ans 
        
        seen = {startGene} #skip extra checking if node in bank
        queue = deque([(startGene, 0)]) #node, steps
        
        while queue:
            
            gene, steps = queue.popleft()
            
            if gene == endGene:
                return steps
            
            for node in neighbours(gene):
                if node not in seen and node in bank:
                    seen.add(node)
                    queue.append([node, steps+1]) 
        
        return -1
