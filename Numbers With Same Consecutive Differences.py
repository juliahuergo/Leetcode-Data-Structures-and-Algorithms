class Solution(object):
    def numsSameConsecDiff(self, n, k):
        def backtrack(curr, i):
            if len(curr) == n:
                ans.append(int("".join(map(str, curr))))
                return
            
            for num in range(0, 10):
                if i==0 and num==0: continue
                elif (i==0 and num!=0) or abs(num-curr[i-1]) == k:
                    curr.append(num)
                    backtrack(curr, i+1)
                    curr.pop()
                
        ans = []
        backtrack([], 0)
        return ans
