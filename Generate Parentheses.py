class Solution(object):
    def generateParenthesis(self, n):
        def backtrack(curr):
            if curr.count('(') == curr.count(')') == n:
                ans.append("".join(curr[:]))
                return
            
            for char in ['(',')']:
                if (char == '(' and curr.count('(') < n) or (char == ')' and curr.count('(') > curr.count(')')):
                    curr.append(char)
                    backtrack(curr)
                    curr.pop()
            
            
        ans = []
        backtrack(['('])
        return ans
