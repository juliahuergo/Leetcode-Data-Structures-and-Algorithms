class Trie(object):

    def __init__(self):
        self.root = {} #hash map for trie implementation
        

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["$"] = True
        #creating a hash map that deepens with every letter 

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return "$" in node
        

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node:
                return False
            node = node[c]
        return True
