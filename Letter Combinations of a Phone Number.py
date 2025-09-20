class Solution(object):
    def letterCombinations(self, digits):
        
        def backtrack(curr, i):
            if len(digits) == 0:
                return
            elif len(curr) == len(digits):
                ans.append("".join(curr[:]))
                return 
            
            for letter in map[digits[i]]:
                curr.append(letter)
                backtrack(curr, i+1)
                curr.pop()          
        
        map = {'2':['a', 'b', 'c'],
               '3':['d','e','f'],
               '4':['g','h','i'],
               '5':['j','k','l'],
               '6':['m','n','o'],
               '7':['p','q','r','s'],
               '8':['t','u','v'],
               '9':['w','x','y','z']}
        
        ans = []
        backtrack([], 0)
        return ans
