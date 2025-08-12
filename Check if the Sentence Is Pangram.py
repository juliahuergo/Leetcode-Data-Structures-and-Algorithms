class Solution(object):
    def checkIfPangram(self, sentence):
        sentence = set(sentence)
        for letter in string.ascii_lowercase:
            if letter not in sentence:
                return False            
        return True
        
