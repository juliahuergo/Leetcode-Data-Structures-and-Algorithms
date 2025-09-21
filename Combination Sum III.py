class Solution(object):
    def combinationSum3(self, k, n):
        def backtrack(i, path, curr):
            if len(path) == k:
                if curr == n:
                    ans.append(path[:])
                return
            
            
            for num in range(i, 10):
                if curr + num <= n:
                    path.append(num)
                    backtrack(num+1, path, curr+num)
                    path.pop()           
            
            
        ans = []
        backtrack(1,[], 0)
        return ans
