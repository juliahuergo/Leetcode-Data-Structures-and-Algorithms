class Solution(object):
    def makeGood(self, s):
        stack = []
        
        for letter in s:
            if stack and letter != stack[-1] and letter.lower() == stack[-1].lower():
                stack.pop()
            else:
                stack.append(letter)
        
        return "".join(stack)
