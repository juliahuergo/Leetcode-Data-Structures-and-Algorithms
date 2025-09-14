class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
        
        def connected(word1, word2):
            count = 0
            for i in range(len(word1)):
                if (word1[i] != word2[i]):
                    count += 1
            return count == 1
        
        def neighbours(node):
            ans = []
            for word in wordSet:
                if connected(node, word):
                    ans.append(word)
            return ans
        
        queue = deque([(beginWord, 1)])
        seen = {beginWord}
        
        while queue:
            node, steps = queue.popleft()
            
            if node == endWord:
                return steps
            
            for word in neighbours(node):
                if word not in seen:
                    wordSet.remove(word)
                    seen.add(word)
                    queue.append([word, steps+1])
        
        return 0
        
        
