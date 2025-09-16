class Solution(object):
    def maximum69Number (self, num):
        initial = str(num)
        for i in range(len(initial)):
            if initial[i] != '9':
                return int(initial[:i]+'9'+initial[i+1:])
        return num
